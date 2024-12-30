class Match:
    def __init__(self, bey1, bey2):
        self._battles = 0
        self._bey1 = bey1
        self._bey2 = bey2
        self._bey1_points = 0
        self._bey2_points = 0
        self._winner = None
    
    def get_bey1_points(self):
        return self._bey1_points
    
    def get_bey2_points(self):
        return self._bey2_points
    
    def get_winner(self):
        if (self._bey1_points >= 4):
            self.winner = self.bey1
        elif (self._bey2_points >= 4):
            self._winner = self._bey2
        else:
            self._winner = None
        return self._winner
    
    def get_bey1(self):
        return self._bey1
    
    def get_bey2(self):
        return self._bey2