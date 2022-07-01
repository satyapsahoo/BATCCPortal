class Players:

    def __init__(self):
        self.player_list = []
        self.image_list = []
        self.number_players = int()

    def get_falcons(self):
        # Clear the player and image list as it might mix up falcon and lion players
        self.player_list.clear()
        self.image_list.clear()
        # Dictionary of all falcon player, to be manually updated. Match the value with the image file name
        players_dict = {
            "Default": "default",
            "Dinesh Sasi Kumar": "dinesh",
            "Vineet Bhola": "vineet",
            "Sasi Kiran Alur": "sasi",
            "Nitin Madan": "nitin",
            "Yeshodhara Baskaran": "yeshodhara",
            "Rohit Kumar Goyal": "rohit",
            "Satya Prakash Sahoo": "satya",
            "Zeeshan Sami": "zeeshan",
            "Amit Rajendra Desai": "amit",
            "Sriraman Ravi": "sriraman",
            "Sanjeev Sivaraman": "sanjeev",
            "Gundeep Singh": "gundeep",
            "Praveen Benni": "praveen2",
            "Harsh Mulrav": "harsh",
            "Saikiran Gundaboina": "saikiran",
            "Vinod Siddarajaiah": "vinod",
            "Rhys Robinson": "rhys",
            "Vineep Bhat": "vineep",
            "Ashish Satpathy": "ashish",
            "Bhavin Kantilal Solanki": "bhavin",
            "Praveen Kumar Daneti": "praveen1",
            "Raghavendra Bheemaiah": "raghavendra",
            "Shashidhara Hanumaiah Veerabhadraiah": "shashidhara",
        }

        for player in players_dict:
            self.player_list.append(player)
            self.image_list.append(players_dict[player])
        self.number_players = len(self.player_list)
        # return self.player_list, self.image_list, self.number_players

    def get_lions(self):
        # Clear the player and image list as it might mix up falcon and lion players
        self.player_list.clear()
        self.image_list.clear()
        # Dictionary of all falcon player, to be manually updated. Match the value with the image file name
        players_dict = {
            "Default": "default",
            "Dinesh Sasi Kumar": "dinesh",
            "Vineet Bhola": "vineet",
            "Sasi Kiran Alur": "sasi",
            "Nitin Madan": "nitin",
            "Yeshodhara Baskaran": "yeshodhara",
            "Rohit Kumar Goyal": "rohit",
            "Satya Prakash Sahoo": "satya",
            "Zeeshan Sami": "zeeshan",
            "Amit Rajendra Desai": "amit",
            "Sriraman Ravi": "sriraman",
            "Sanjeev Sivaraman": "sanjeev",
            "Gundeep Singh": "gundeep",
            "Praveen Benni": "praveen2",
            "Harsh Mulrav": "harsh",
            "Saikiran Gundaboina": "saikiran",
            "Vinod Siddarajaiah": "vinod",
            "Rhys Robinson": "rhys",
            "Vineep Bhat": "vineep",
            "Ashish Satpathy": "ashish",
            "Bhavin Kantilal Solanki": "bhavin",
            "Praveen Kumar Daneti": "praveen1",
            "Raghavendra Bheemaiah": "raghavendra",
            "Shashidhara Hanumaiah Veerabhadraiah": "shashidhara",
        }

        for player in players_dict:
            self.player_list.append(player)
            self.image_list.append(players_dict[player])
        self.number_players = len(self.player_list)
        # return self.player_list, self.image_list, self.number_players

    def get_image_file(self, player_name):
        # Get image file name from the player profile page and return the image file name
        player_name = str(player_name.title())
        self.get_falcons()
        try:
            index = self.player_list.index(player_name)
        except ValueError:
            self.get_lions()
            try:
                index = self.player_list.index(player_name)
            except ValueError:
                index = 0
        return self.image_list[index]

