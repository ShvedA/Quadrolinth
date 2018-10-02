class Game:
    def __init__(self):
        self.players = []
        self.turn = 0

    def add_player(self, player):
        self.players.append(player)

    def nr_of_players(self):
        return len(self.players)

    #def end_turn(self):
     #   if check_end_game():


    #def check_end_game(self):
     #   if self.players.count()
