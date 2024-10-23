class Player:
    def __init__(self):
        self.hp = 100
        self.atk = 2
        self.current_room = 0
        self.last_room = 0
        self.key_found = False
        self.has_won = False

    def set_hp(self, n):
        self.hp = n

    def get_hp(self):
        return self.hp

    def set_atk(self, n):
        self.atk = n

    def get_atk(self):
        return self.atk

    def set_current_room(self, n):
        self.current_room = n

    def get_current_room(self):
        return self.current_room

    def set_last_room(self, n):
        self.last_room = n

    def get_last_room(self):
        return self.last_room

    def set_key_found(self, b):
        self.key_found = b

    def has_key(self):
        return self.key_found
    
    def set_winner(self, b):
        self.has_won = b

    def attack(self, target):
        target.set_hp(target.get_hp() - self.atk)

    def potion_heal(self):
        self.hp += 10

    def is_alive(self):
        return self.hp > 0
    
    def has_key(self):
        return self.key_found
    
    def is_winner(self):
        return self.has_won