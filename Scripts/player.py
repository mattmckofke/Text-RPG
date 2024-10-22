class Player:
    def __init__(self, hp=100, atk=2, current_room=0, last_room=0, key_found=False):
        self.hp = hp
        self.atk = atk
        self.current_room = current_room
        self.last_room = last_room
        self.key_found = key_found

    def set_hp(self, hp):
        self.hp = hp

    def get_hp(self):
        return self.hp

    def set_atk(self, atk):
        self.atk = atk

    def get_atk(self):
        return self.atk

    def set_current_room(self, current_room):
        self.current_room = current_room

    def get_current_room(self):
        return self.current_room

    def set_last_room(self, last_room):
        self.last_room = last_room

    def get_last_room(self):
        return self.last_room

    def set_key_found(self, key_found):
        self.key_found = key_found

    def has_key(self):
        return self.key_found

    def attack(self, target):
        target.set_hp(target.get_hp() - self.atk)

    def potion_heal(self):
        self.hp += 10

    def is_alive(self):
        return self.hp > 0
    
    def has_key(self):
        return self.key_found