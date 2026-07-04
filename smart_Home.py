class smartBulb:
    def __init__(self):
        self.is_On = False
        self.Brightness = 0
    def turn_On(self):
        self.is_On = True
        self.Brightness = 100
    def trun_Off(self):
        self.is_On = False
        self.Brightness = 0