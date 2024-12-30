from victory import Victory

class Match:
    def __init__(self, bey1, bey2):
        self._battles = 0
        self._bey1 = bey1
        self._bey2 = bey2
        self._bey1_points = 0
        self._bey2_points = 0
        self._winner = None
    
    def get_battles(self):
        return self._battles
    
    def get_bey1_points(self):
        return self._bey1_points
    
    def get_bey2_points(self):
        return self._bey2_points
    
    def increment_battles(self):
        self._battles += 1
    
    def decide_winner(self):
        if (self._bey1_points >= 4):
            self._winner = self._bey1
        elif (self._bey2_points >= 4):
            self._winner = self._bey2
        else:
            self._winner = None
    
    def battle(self):
        while (self._winner is None):
            self.increment_battles()
            print(f"Battle: {self._battles}")
            print("Enter 1 for your beyblade, 2 for your opponent's beyblade")
            win = int(input())
            print("Enter the type of victory")
            wt = ""

            while not(wt == "spin" or wt == "over" or 
                        wt == "burst" or wt == "x"):
                wt = input()
            if (win == 1):
                self._bey1.add_win(wt)
                self._bey1_points += self.points_calc(wt)
                print(f"{self._bey1.__str__()} wins by {wt} finish!")

            elif (win == 2):
                self._bey2.add_win(wt)
                self._bey2_points += self.points_calc(wt)
                print(f"{self._bey2.__str__()} wins by {wt} finish!")

            self.decide_winner()
        print(f"{self._winner.__str__()} wins the match!")
    
    def points_calc(self, wt):
        if (wt == "spin"):
            return 1
        elif (wt == "over" or wt == "burst"):
            return 2
        elif (wt == "x"):
            return 3
        else:
            return 0
    
    def get_bey1(self):
        return self._bey1
    
    def get_bey2(self):
        return self._bey2