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
                       3: "You attacked the giant rat. (How did it get so big?)",
                       4: "You turn back and head to the room you started in."},
                   3: {1: "You inspect the room and see a chest in the corner. You open it and find a sword! (Wait, you've been attacking with your fists this whole time?)",
                       2: "You drink a potion and heal yourself.",
                       3: "You go back to the last room.",
                       4: "You go to the next room."},
                   4: {1: "You inspect the room and see a door at the far end of it. You need to get over there!",
                       2: "You drink a potion and heal yourself.",
                       3: "You attack the dragon. (HOW STRONG IS THIS THING???)",
                       4: "You go back to the last room."}
                   }

def update_ops_list(pl):
    if not pl.rat_is_alive():
        num_ops_list[2] = 5
    if pl.has_key():
        num_ops_list[4] = 5
    if not pl.dragon_is_alive():
        num_ops_list[4] = 3
    if pl.has_won:
        num_ops_list[4] = 5
        
def update_chosen_ops_list(pl):
    if not pl.rat_is_alive():
        chosen_ops_list[2] = {1: "You inspect the room and see a door on the other side of it.",
                              2: "You drink a potion and heal yourself.",
                              4: "You turn back and head to the room you started in.",
                              5: "You go to the next room."}
    if pl.has_key() and pl.dragon_is_alive():
        chosen_ops_list[4] = {1: "You inspect the room and see a door at the far end of it. You need to get over there!",
                              2: "You drink a potion and heal yourself.",
                              3: "You attacked the dragon. (HOW STRONG IS THIS THING???)",
                              4: "You go back to the last room.",
                              6: "You use the key from the skeleton to unlock the door and walk through."}
    elif pl.has_key() and not pl.dragon_is_alive():
        chosen_ops_list[4] = {1: "You inspect the room and see a door at the far end of it. You need to get over there!",
                              2: "You drink a potion and heal yourself.",
                              4: "You go back to the last room.",
                              5: "You go to the next room.",
                              6: "You use the key from the skeleton to unlock the door and walk through."}
    elif not pl.has_key() and not pl.dragon_is_alive():
        chosen_ops_list[4] = {1: "You inspect the room and see a door at the far end of it. You need to get over there!",
                              2: "You drink a potion and heal yourself.",
                              4: "You go back to the last room.",
                              5: "You go to the next room."}

def update_current_room(pl, choice):
    if pl.current_room == 0:
        update_start_room(pl, choice)
    elif pl.current_room == 1:
        update_room_1(pl, choice)
    elif pl.current_room == 2:
        update_room_2(pl, choice)
    elif pl.current_room == 3:
        update_room_3(pl, choice)
    elif pl.current_room == 4:
        update_room_4(pl, choice)

def update_start_room(pl, choice):
    if choice == 3:
        pl.current_room = 1
    elif choice == 4:
        pl.current_room = 2

def update_room_1(pl, choice):
    if choice == 3:
        pl.current_room = 0

def update_room_2(pl, choice):
    if choice == 4:
        pl.current_room = 0
    elif choice == 5:
        pl.current_room = 3

def update_room_3(pl, choice):
    if choice == 3:
        pl.current_room = 2
    elif choice == 4:
        pl.current_room = 4

def update_room_4(pl, choice):
    if choice == 4:
        pl.current_room = 3

def start_room():
    print("This is the room your adventure starts in. What do you do?")
    print("1. Inspect the room")
    print("2. Heal")
    print("3. Go to room 1")
    print("4. Go to room 2")
    
def room_1():
    print("You enter the room. What do you do?")
    print("1. Inspect the room")
    print("2. Heal")
    print("3. Go back to the start room")

def room_2(pl):
    print("You enter the room. There is a giant rat blocking your way! What do you do?")
    print("1. Inspect the room")
    print("2. Heal")
    if pl.rat_is_alive():
        print("3. Attack the giant rat")
        print("4. Go back to the start room")
    else:
        print("4. Go back to the start room")
        print("5. Go to the next room")

def room_3():
    print("You enter the room expecting an enemy and find none. What do you do?")
    print("1. Inspect the room")
    print("2. Heal")
    print("3. Go back to the last room")
    print("4. Go to the next room")

def room_4(pl):
    print("You enter the room. There is a huge dragon in front of you! What do you do?")
    print("1. Inspect the room")
    print("2. Heal")
    if pl.dragon_is_alive():
        print("3. Attack the dragon")
        print("4. Go back to the last room")
    else:
        print("4. Go back to the last room")
        print("5. Go to the next room")
    if pl.has_key():
        print("6. ???")

def end_room():
    print("You have beaten the game! Congratulations!")
    print("Thanks for playing!")
    
# LOGIC FUNCTIONS
#-----------------

def logic_start(pl, choice):
    print(chosen_ops_list.get(0).get(choice))
    if choice == 2:
        pl.potion_heal()
    

def logic_1(pl, choice):
    print(chosen_ops_list.get(1).get(choice))
    if choice == 1:
        pl.set_key_found(True)
    if choice == 2:
        pl.potion_heal()

# update with new rat functionality
def logic_2(pl, choice):
    print(chosen_ops_list.get(2).get(choice))
    if choice == 2:
        pl.potion_heal()
    if choice == 3 and pl.rat_is_alive():
        pl.attack_rat()
        
def logic_3(pl, choice):
    print(chosen_ops_list.get(3).get(choice))
    if choice == 2:
        pl.potion_heal()

# update with new dragon functionality
def logic_4(pl, choice):
    print(chosen_ops_list.get(4).get(choice))
    if choice == 2:
        pl.potion_heal()
    elif choice == 3 and pl.dragon_is_alive():
        pl.attack_dragon()
    elif choice == 5:
        pl.set_winner(True)
    elif choice == 6 and pl.has_key():
        print("You unlock the door and walk through. There was nothing here, what a waste of a secret. You immediately leave the room, feeling disappointed.")