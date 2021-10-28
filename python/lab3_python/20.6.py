class bet_log:
    betted = list()

    def do_bet(self, horse, bet):
        if horse > 10 or horse in self.betted or bet == 0:
            print("error")
        print(bet, "for horse #" + str(horse))
        self.betted.append(horse)
