class Victory:
    def __init__(self, bey, wt):
        self._bey = bey
        self._wt = wt
        self._points = 0
        self._assign_points(wt)

    def get_bey(self):
        return self._bey
    
    def get_wt(self):
        return self._wt
    
    def get_points(self):
        return self._points
    
    def __str__(self):
        return f"{self._bey} wins by {self._wt} finish!"
    
    def _assign_points(self, wt):
        if (wt == "spin"):
            self._points = 1
        elif (wt == "over" or wt == "burst"):
            self._points = 2
        elif (wt == "x"):
            self._points = 3
        else:
            self._points = 0