class kampfposition():
    def __init__(self, Position = 'stehend'):
        self.Position = Position
        
    def neu(self,Position):
        self.Position = Position
        
    def eigen(self):
        if self.Position == 'Stehend': return 0
        elif self.Position == 'Kniend, Fernkampf': return 0
        elif self.Position == 'Kniend, Nahkampf': return -3
        elif self.Position == 'Liegend, Armbrust': return  0
        elif self.Position == 'Liegend, anderer Fernkampf': return  -6
        elif self.Position == 'Liegend, Nahkampf': return  -6
        elif self.Position == 'Fliegend': return +3
        else: return 0
        
    def gegner(self):
        if self.Position == 'Stehend': return 0
        elif self.Position == 'Kniend, Fernkampf': return -3
        elif self.Position == 'Kniend, Nahkampf': return 3
        elif self.Position == 'Liegend, Armbrust': return  -6
        elif self.Position == 'Liegend, anderer Fernkampf': return  -6
        elif self.Position == 'Liegend, Nahkampf': return  +6
        elif self.Position == 'Fliegend': return -3
        else: return 0