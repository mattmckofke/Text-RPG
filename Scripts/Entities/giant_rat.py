class giant_rat:
    def __init__(self):
        self.hp = 20
        self.atk = 5
    
    def set_hp(self, n):
        self.hp = n
    
    def set_atk(self, n):
        self.atk = n
        
    def attack_player(self, pl):
        pl.set_hp(pl.hp - self.atk)
    
    def is_alive(self):
        return self.hp > 0