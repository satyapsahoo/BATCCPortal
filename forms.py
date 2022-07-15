from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, DateField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm
class RegisterForm(FlaskForm):
    email = EmailField("Email*", validators=[DataRequired()])
    password = PasswordField("Password*", validators=[DataRequired()])
    name = StringField("Name*", validators=[DataRequired()])
    address = StringField("Address")
    dress_size = StringField("Dress Size S/M/L/XL")
    dob = DateField("Date of Birth*")
    passport = StringField("Passport Number")
    strength = CKEditorField("Strength Area")
    weakness = CKEditorField("Weakness Area")
    improvements = CKEditorField("Improvement Area")
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let me in")


class EditForm(FlaskForm):
    name = StringField("Name")
    address = StringField("Address")
    dress_size = StringField("Dress Size S/M/L/XL")
    passport = StringField("Passport Number")
    strength = CKEditorField("Strength Area")
    weakness = CKEditorField("Weakness Area")
    improvements = CKEditorField("Improvement Area")
    submit = SubmitField("Submit")


class AdminForm(FlaskForm):
    name = StringField("Name")
    strength = CKEditorField("Strength Area")
    weakness = CKEditorField("Weakness Area")
    improvements = CKEditorField("Improvement Area")
    address = StringField("Address")
    dress_size = StringField("Dress Size S/M/L/XL")
    passport = StringField("Passport Number")
    submit = SubmitField("Submit")


class ResetPassword(FlaskForm):
    name = StringField("Name")
    submit = SubmitField("Reset Password")


class ChangePassword(FlaskForm):
    password = PasswordField("Enter New Password", validators=[DataRequired()])
    submit = SubmitField("Change Password")


class AnnouncementForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    body = CKEditorField("Content", validators=[DataRequired()])
    submit = SubmitField("Submit")
