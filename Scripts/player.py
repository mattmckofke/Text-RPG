class player:
    def __init__(self):
        self.hp = 100
        self.atk = 2
        self.current_room = 0
        self.key_found = False
        self.has_won = False
        self.rat_hits = 0
        self.dragon_hits = 0

    def set_hp(self, n):
        self.hp = n

    def set_atk(self, n):
        self.atk = n

    def set_current_room(self, n):
        self.current_room = n

    def set_key_found(self, b):
        self.key_found = b

    def has_key(self):
        return self.key_found
    
    def set_winner(self, b):
        self.has_won = b

    def attack_rat(self):
        self.rat_hits += 1
        if self.rat_hits == 3:
            print("You killed the rat!")
        elif self.rat_hits < 3:
            print("You attacked the rat!")
    
    def attack_dragon(self):
        self.dragon_hits += 1
        if self.dragon_hits == 10:
            print("You killed the dragon!")
        elif self.dragon_hits < 10:
            print("You attacked the dragon!")
            
    # add functions to handle rat and dragon attacking player
    # currently not used
    def rat_attack(self):
        self.hp -= 5
        print("The rat attacked you for 5 hit points!")
        if not self.is_alive():
            print("You died to the rat!")
            
    # currently not used
    def dragon_attack(self):
        self.hp -= 10
        print("The dragon attacked you for 10 hit points!")
        if not self.is_alive():
            print("You died to the dragon!")

    # currently not used
    def potion_heal(self):
        if self.hp == 100:
            print("You are already at full health!")
        elif (self.hp + 10) > 100:
            self.hp = 100
        else:
            self.hp += 10

    def is_alive(self):
        return self.hp > 0
    
    def rat_is_alive(self):
        return self.rat_hits < 3
    
    def dragon_is_alive(self):
        return self.dragon_hits < 10