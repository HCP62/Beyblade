from match import Match

class TestSession:
    def __init__(self, bey1, bey2):
        self._matches = []
        self._total_battles = [i.get_battles() for i in self._matches]
        self._bey1 = bey1
        self._bey2 = bey2
        self._bey1_wr = self.calc_wr(bey1)
        self._bey2_wr = self.calc_wr(bey2)
    
    def get_bey_wr(self, bey):
        if (bey == self._bey1):
            return self._bey1_wr
        elif (bey == self._bey2):
            return self._bey2_wr
        else:
            return 0.0
    
    def start_session(self):
        for i in range(10):
            match.increment_battles()
            match = Match(self._bey1, self._bey2)
            print("Enter 1 for your beyblade, 2 for your opponent's beyblade")
            win = int(input())
            print("Enter the type of victory")
            wt = ""
            while not(wt == "spin" or wt == "over" or 
                      wt == "burst" or wt == "x"):
                wt = input()
            if (win == 1):
                self._bey1.add_win(wt)
            elif (win == 2):
                self._bey2.add_win(wt)

    def calc_wr(self):
        return float(len(self._bey1.get_wins()) / len(self._total_battles)) * 100
    
    def calc_by_type(self, wt):
        return float(self._bey1.get_win_by_type(wt) / self._total_battles) * 100