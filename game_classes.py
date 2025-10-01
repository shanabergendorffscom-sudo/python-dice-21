from helpers import roll_dice

class Player:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.busted = False

    def reset(self):
        self.total = 0
        self.busted = False

    def roll(self):
        value = roll_dice()
        self.total += value
        if self.total > 21:
            self.busted = True
        return value

class Game:
    def __init__(self):
        self.player = Player("Player")
        self.dealer = Player("Dealer")
        self.scores = self.load_scores()

    def load_scores(self):
        try:
            with open("highscore.txt", "r") as f:
                lines = f.readlines()
                return {
                    "Player": int(lines[0].split(":")[1]),
                    "Dealer": int(lines[1].split(":")[1])
                }
        except:
            return {"Player": 0, "Dealer": 0}

    def save_scores(self):
        with open("highscore.txt", "w") as f:
            f.write(f"Player:{self.scores['Player']}\n")
            f.write(f"Dealer:{self.scores['Dealer']}\n")

    def play_dealer_turn(self):
        self.dealer.reset()
        while self.dealer.total < 17:
            self.dealer.roll()
        return self.dealer.total
