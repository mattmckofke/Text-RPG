from Scripts import rooms
from Scripts.Entities import player, giant_rat, dragon

pl = player.player()
gr = giant_rat.giant_rat()
d = dragon.dragon()

# dictionary tied to functions to handle all rooms
rms = {
        0: rooms.start_room,
        1: rooms.room_1,
        2: lambda: rooms.room_2(pl, gr),
        3: rooms.room_3,
        4: lambda: rooms.room_4(pl, d),
        5: rooms.end_room
    }    

# dictionary tied to functions to handle all logic
rms_helpers = {
        0: rooms.logic_start,
        1: rooms.logic_1,
        2: rooms.logic_2,
        3: rooms.logic_3,
        4: rooms.logic_4,
        5: rooms.logic_end
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
        
        #if player is in start room, call function to handle start room logic (pass in player and choice)
        if pl.current_room == 0:
            rms_helpers[0](pl, choice)
        
        # if player is in room 1, call function to handle room 1 logic (pass in player and choice)
        if pl.current_room == 1:
            rms_helpers[1](pl, choice)
            
        # else if player is in room 2, call function to handle room 2 logic (pass in player, giant_rat, and choice)
        elif pl.current_room == 2:
            rms_helpers[2](pl, gr, choice)
            
        # else if player is in room 3, call function to handle room 3 logic (pass in player and choice)
        elif pl.current_room == 3:
            rms_helpers[3](pl, choice)
            
        # else if player is in room 4, call function to handle room 4 logic (pass in player, dragon, and choice)
        elif pl.current_room == 4:
            rms_helpers[4](pl, d, choice)
            
        # else (this is when player is in room 5) call rooms.end_room() (no logic to be handled here)
        else:
            rms[5]()
        
        # update dictionaries
        rooms.update_ops_list(pl, gr, d)
        rooms.update_chosen_ops_list(pl, gr, d)
        
        # update current room
        rooms.update_current_room(pl, choice)

run_game()