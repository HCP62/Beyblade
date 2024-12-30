from victory import Victory

class Beyblade:
    def __init__(self, blade, ratchet, bit):
        self._blade = blade
        self._ratchet = ratchet
        self._bit = bit
        self._wins = self.init_dict()
    
    def init_dict(self):
        return {
            "spin": [],
            "over": [],
            "burst": [],
            "x": []
        }
    
    def get_blade(self):
        return self._blade
    
    def get_wins(self):
        return self._wins

    def get_ratchet(self):
        return self._ratchet

    def get_bit(self):
        return self._bit
    
    def add_win(self, wt):
        self._wins[wt].append(Victory(self, wt))
    
    def get_win_by_type(self, wt):
        return len(self._wins[wt])

    def __str__(self):
        return f"{self._blade} {self._ratchet}{self._bit}"

    def __eq__(self, other):
        return self._blade == other._blade and \
            self._ratchet == other._ratchet and \
            self._bit == other._bit