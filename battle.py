from victory import Victory
from beyblade import Beyblade

class Battle:
    def __init__(self, bey1, bey2):
        self._bey1 = bey1
        self._bey2 = bey2
        self._winner = None
    
    
    def get_winner(self):
        return self._winner