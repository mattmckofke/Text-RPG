class player:
    def __init__(self):
        self.hp = 100
        self.atk = 2
        self.current_room = 0
        self.last_room = 0
        self.key_found = False
        self.has_won = False

    def set_hp(self, n):
        self.hp = n

    def set_atk(self, n):
        self.atk = n

    def set_current_room(self, n):
        self.current_room = n

    def set_last_room(self, n):
        self.last_room = n

    def set_key_found(self, b):
        self.key_found = b

    def has_key(self):
        return self.key_found
    
    def set_winner(self, b):
        self.has_won = b

    def attack_rat(self, gr):
        gr.set_hp(gr.hp - self.atk)
    
    def attack_dragon(self, d):
        d.set_hp(d.hp - self.atk)

    def potion_heal(self):
        if self.hp == 100:
            print("You are already at full health!")
        elif (self.hp + 10) > 100:
            self.hp = 100
        else:
            self.hp += 10

    def is_alive(self):
        return self.hp > 0