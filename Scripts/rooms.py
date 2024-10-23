import player

num_ops_list = [4, 3, 3, 4, 4]

chosen_ops_list = {0: {1: "You inspect the room and see nothing useful.",
                       2: "You drink a potion and heal yourself.",
                       3: "You head to the left door and open it, wondering what could be on the other side.",
                       4: "You head to the right door and open it, wondering what could be on the other side."},
                   1: {1: "You inspect the room, and see a skeleton sitting in the corner with a gold key around it's neck. It might be useful later.",
                       2: "You drink a potion and heal yourself.",
                       3: "You turn back and head to the room you started in."},
                   2: {1: "You inspect the room and see a door on the other side of it.",
                       2: "You drink a potion and heal yourself.",
                       3: "You attack the giant rat. (How did it get so big?)",
                       4: "You turn back and head to the room you started in."},
                   3: {1: "You inspect the room and see a chest in the corner. You open it and find a sword! (Wait, you've been attacking with your fists this whole time?)",
                       2: "You drink a potion and heal yourself.",
                       3: "You go back to the last room."},
                   4: {1: "You inspect the room and see a door at the far end of it. You need to get over there!",
                       2: "You drink a potion and heal yourself.",
                       3: "You attack the dragon. (HOW STRONG IS THIS THING???)",
                       4: "You go back to the last room."}
                   }

def update_ops_list(pl):
    if pl.killed_skeleton():
        num_ops_list[2] = 4
    if pl.has_key():
        num_ops_list[4] = 5
        
def update_chosen_ops_list(pl):
    if pl.killed_skeleton():
        chosen_ops_list[2] = {1: "You inspect the room and see a door on the other side of it.",
                              2: "You drink a potion and heal yourself.",
                              3: "You attack the giant rat. (How did it get so big?)",
                              4: "You turn back and head to the room you started in.",
                              5: "You go to the next room."}
    if pl.has_key():
        chosen_ops_list[4] = {1: "You inspect the room and see a door at the far end of it. You need to get over there!",
                              2: "You drink a potion and heal yourself.",
                              3: "You attack the dragon. (HOW STRONG IS THIS THING???)",
                              4: "You go back to the last room.",
                              5: "You use the key from the skeleton to unlock the door and walk through."}

def start_room(pl):
    pl.current_room = 0
    print("This is the room your adventure starts in. What do you do?")
    print("1. Inspect the room")
    print("2. Heal")
    print("3. Go to room 1")
    print("4. Go to room 2")
    
def room_1(pl):
    pl.current_room = 1
    print("You enter the room. What do you do?")
    print("1. Inspect the room")
    print("2. Heal")
    print("3. Go back to the start room")
    
def room_2(pl):
    pl.current_room = 2
    print("You enter the room. There is a giant rat blocking your way! What do you do?")
    print("1. Inspect the room")
    print("2. Heal")
    print("3. Attack the rat")
    print("4. Go back to the start room")
    if pl.killed_skeleton():
        print("5. Go to the next room")

def room_3(pl):
    pl.current_room = 3
    print("You enter the room expecting an enemy and find none. What do you do?")
    print("1. Inspect the room")
    print("2. Heal")
    print("3. Go back to the last room")
    print("4. Go to the next room")

def room_4(pl):
    pl.current_room = 4
    print("You enter the room. There is a huge dragon in front of you! What do you do?")
    print("1. Inspect the room")
    print("2. Heal")
    print("3. Attack the dragon")
    print("4. Go back to the last room")
    if pl.has_key():
        print("5. ???")

def end_room(pl):
    pl.current_room = 5
    print("You have beaten the game! Congratulations!")
    print("Thanks for playing!")