class Players:

    def __init__(self):
        self.player_list = []
        self.image_list = []
        self.number_players = int()

    def get_falcons(self):
        players_dict = {
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

        for player in players_dict:
            self.player_list.append(player)
            self.image_list.append(players_dict[player])
        self.number_players = len(self.player_list)
        return self.player_list, self.image_list, self.number_players

    def get_lions(self):
        players_dict = {
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

        for player in players_dict:
            self.player_list.append(player)
            self.image_list.append(players_dict[player])
        self.number_players = len(self.player_list)
        return self.player_list, self.image_list, self.number_players
