import werkzeug
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_ckeditor import CKEditor
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import RegisterForm, LoginForm, EditForm, AdminForm
from functools import wraps
from flask import abort
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
ckeditor = CKEditor(app)
Bootstrap(app)


# CONNECT TO DB from Heroku
uri = os.environ.get("DATABASE_URL")
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri

# CONNECT TO DB from Pycharm
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL",  "sqlite:///club.db")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


# Create admin-only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)
    return decorated_function


# CONFIGURE TABLES
class User(UserMixin, db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(250))
    dress_size = db.Column(db.String(100))
    dob = db.Column(db.String(100))
    passport = db.Column(db.String(100))
    strength = db.Column(db.Text)
    weakness = db.Column(db.Text)
    improvements = db.Column(db.Text)


# db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                if user.name == "Administrator":
                    return redirect(url_for('admin_page'))
                else:
                    return redirect(url_for('player_profile', player_id=user.id))
            else:
                flash('Invalid password provided')
                return redirect(url_for('login'))
        else:
            flash('Invalid user provided')
            return redirect(url_for('login'))

    return render_template("login.html", form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/register', methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        if User.query.filter_by(email=register_form.email.data).first():
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        new_user = User(
            email=register_form.email.data,
            password=werkzeug.security.generate_password_hash(register_form.password.data, method='pbkdf2:sha256',
                                                              salt_length=8),
            name=register_form.name.data,
            address=register_form.address.data,
            dress_size=register_form.dress_size.data,
            dob=register_form.dob.data,
            passport=register_form.passport.data,
            strength=register_form.strength.data,
            weakness=register_form.weakness.data,
            improvements=register_form.improvements.data,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('player_profile', player_id=new_user.id))

    return render_template("register.html", form=register_form)


@app.route('/player_profile/<player_id>', methods=["GET", "POST"])
@login_required
def player_profile(player_id):
    player = User.query.filter_by(id=player_id).first()
    return render_template("player_profile.html", player=player)


@app.route('/edit_profile', methods=["GET", "POST"])
@login_required
def edit_profile():
    edit_form = EditForm(
        name=current_user.name,
        address=current_user.address,
        dress_size=current_user.dress_size,
        passport=current_user.passport,
        strength=current_user.strength,
        weakness=current_user.weakness,
        improvements=current_user.improvements,
    )
    if edit_form.validate_on_submit():
        current_user.address = edit_form.address.data
        current_user.name = edit_form.name.data
        current_user.dress_size = edit_form.dress_size.data
        current_user.passport = edit_form.passport.data
        current_user.strength = edit_form.strength.data
        current_user.weakness = edit_form.weakness.data
        current_user.improvements = edit_form.improvements.data
        db.session.commit()
        return redirect(url_for('player_profile', player_id=current_user.id))

    return render_template("edit_profile.html", form=edit_form)


@app.route('/admin_page', methods=["GET", "POST"])
@admin_only
def admin_page():
    all_players = User.query.all()
    return render_template("admin_page.html", players=all_players)


@app.route('/admin_edit/<player_id>', methods=["GET", "POST"])
@admin_only
def admin_edit(player_id):
    req_player = User.query.filter_by(id=player_id).first()
    print(req_player.name)
    admin_form = AdminForm(
        name=req_player.name,
        strength=req_player.strength,
        weakness=req_player.weakness,
        improvements=req_player.improvements,
    )
    if admin_form.validate_on_submit():
        req_player.strength = admin_form.strength.data
        req_player.weakness = admin_form.weakness.data
        req_player.improvements = admin_form.improvements.data
        db.session.commit()
        return redirect(url_for('player_profile', player_id=req_player.id))

    return render_template("admin_edit.html", form=admin_form)


@app.route('/batcc_falcons', methods=["GET", "POST"])
def batcc_falcons():
    falcons_dict = {
        "Dinesh Sasi Kumar ": "Dinesh",
        "Vineet Bhola": "Vineet",
        "Sasi Kiran Alur": "Sasi",
        "Nitin Madan": "Nitin",
        "Yeshodhara Baskaran": "Yeshodhara",
        "Rohit Kumar Goyal": "Rohit",
        "Satya Prakash Sahoo": "Satya",
        "Zeeshan Sami": "Zeeshan",
        "Amit Rajendra Desai": "Amit",
        "Sriraman Ravi ": "Sriraman",
        "Sanjeev Sivaraman ": "Sanjeev",
        "Gundeep Singh": "Gundeep",
        "Praveen Benni": "Praveen2",
        "Harsh Mulrav": "Harsh",
        "Saikiran Gundaboina": "Saikiran",
        "Vinod Siddarajaiah": "Vinod",
        "Rhys Robinson": "Rhys",
        "Vineep Bhat": "Vineep",
        "Ashish Satpathy": "Ashish",
        "Bhavin Kantilal Solanki": "Bhavin",
        "Praveen Kumar Daneti": "Praveen1",
        "Raghavendra Bheemaiah": "Raghavendra",
        "Shashidhara Hanumaiah Veerabhadraiah": "Shashidhara",
    }

    player_list = []
    image_list = []
    for player in falcons_dict:
        player_list.append(player)
        image_list.append(falcons_dict[player])
    number_players = len(player_list)
    return render_template("batcc_falcons.html", players=player_list, images=image_list, number_players=number_players)


@app.route('/batcc_lions', methods=["GET", "POST"])
def batcc_lions():
    lions_dict = {
        "Dinesh Sasi Kumar ": "Dinesh",
        "Vineet Bhola": "Vineet",
        "Sasi Kiran Alur": "Sasi",
        "Nitin Madan": "Nitin",
        "Yeshodhara Baskaran": "Yeshodhara",
        "Rohit Kumar Goyal": "Rohit",
        "Satya Prakash Sahoo": "Satya",
        "Zeeshan Sami": "Zeeshan",
        "Amit Rajendra Desai": "Amit",
        "Sriraman Ravi ": "Sriraman",
        "Sanjeev Sivaraman ": "Sanjeev",
        "Gundeep Singh": "Gundeep",
        "Praveen Benni": "Praveen2",
        "Harsh Mulrav": "Harsh",
        "Saikiran Gundaboina": "Saikiran",
        "Vinod Siddarajaiah": "Vinod",
        "Rhys Robinson": "Rhys",
        "Vineep Bhat": "Vineep",
        "Ashish Satpathy": "Ashish",
        "Bhavin Kantilal Solanki": "Bhavin",
        "Praveen Kumar Daneti": "Praveen1",
        "Raghavendra Bheemaiah": "Raghavendra",
        "Shashidhara Hanumaiah Veerabhadraiah": "Shashidhara",
    }

    player_list = []
    image_list = []
    for player in lions_dict:
        player_list.append(player)
        image_list.append(lions_dict[player])
    number_players = len(player_list)
    return render_template("batcc_lions.html", players=player_list, images=image_list, number_players=number_players)


if __name__ == "__main__":
    app.run(debug=True)