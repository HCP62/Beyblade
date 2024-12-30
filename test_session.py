from match import Match

class TestSession:
    def __init__(self, bey1, bey2):
        self._total_battles = 0
        self._bey1 = bey1
        self._bey2 = bey2
    
    def start_session(self):
        rem = 0
        while (rem < 10):
            print(f"Match: {rem + 1}")
            match = Match(self._bey1, self._bey2)
            match.battle()
            self._total_battles += match.get_battles()
            rem += 1
        
        """these things are not working"""
        print(f"{self._bey1.__str__()}: {self.calc_wr()}%")
        print(f"{self._bey1.__str__()} spin: {self.calc_by_type('spin')}%")
        print(f"{self._bey1.__str__()} over: {self.calc_by_type('over')}%")
        print(f"{self._bey1.__str__()} burst: {self.calc_by_type('burst')}%")
        print(f"{self._bey1.__str__()} x: {self.calc_by_type('x')}%")

    """meaning this isn't working"""
    def calc_wr(self):
        return float(self._bey1.get_total_wins() / self._total_battles) * 100
    
    def calc_by_type(self, wt):
        return float(self._bey1.get_win_by_type(wt) / self._total_battles) * 100