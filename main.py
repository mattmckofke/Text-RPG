from Scripts import rooms, player

pl = player.player()

# dictionary tied to functions to handle all rooms
rms = {
        0: rooms.start_room,
        1: rooms.room_1,
        2: rooms.room_2,
        3: rooms.room_3,
        4: lambda: rooms.room_4(pl),
        5: rooms.end_room
    }    

# dictionary tied to functions to handle all logic
rms_helpers = {
        0: rooms.logic_start,
        1: rooms.logic_1,
        2: rooms.logic_2,
        3: rooms.logic_3,
        4: rooms.logic_4
    }

def run_game():
    
    # while player is not winner and player is alive
    while not pl.has_won and pl.is_alive():
        rms[pl.current_room]()
        
        # try to get a choice from the player
        try:
            choice = int(input("What do you do? "))
            
            # need to check if choice is in the range of the value in the num_ops_list variable
            if choice not in range(1, rooms.num_ops_list[pl.current_room]+1):
                raise ValueError
        except ValueError:
            print("That's not a choice. Try again.")
            continue
        
        # now need to handle the choice
        
        match pl.current_room:
            case 0:
                rms_helpers[0](pl, choice)
            case 1:
                rms_helpers[1](pl, choice)
            case 2:
                rms_helpers[2](pl, choice)
            case 3:
                rms_helpers[3](pl, choice)
            case 4:
                rms_helpers[4](pl, choice)
            case _:
                rms[5]()
        
        # update dictionaries
        rooms.update_ops_list(pl)
        rooms.update_chosen_ops_list(pl)
        
        # update current room
        rooms.update_current_room(pl, choice)

run_game()