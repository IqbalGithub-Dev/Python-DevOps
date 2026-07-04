#Generating a coffee machine 
class coffe_Machine():
    def __init__(self):
        self.water_Level = 100
        self.bean_Level = 50
    def make_coffe(self):
        if self.water_Level < 20 or self.bean_Level < 10:
            raise ValueError("WARNING PLEASE REFILL WATER AND BEANS")
        
        self.water_Level -=20
        self.bean_Level -= 10