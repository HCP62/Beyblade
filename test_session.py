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
            match = Match(self._bey1, self._bey2)
            
    
    def calc_wr(self, bey):
        return len(bey.get_wins()) / len(self._total_battles)