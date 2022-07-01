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
        # Clear the player and image list as it might mix up falcon and lion players
        self.player_list.clear()
        self.image_list.clear()
        # Dictionary of all falcon player, to be manually updated. Match the value with the image file name
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

    def image_file(self, player_name):
        # Get image file name from the player profile page and return the image file name
        self.get_falcons()
        for player in self.player_list:
            if player == player_name:
                index = self.player_list.index(player)
                return self.image_list[index]

        self.get_lions()
        for player in self.player_list:
            if player == player_name:
                index = self.player_list.index(player)
                return self.image_list[index]
