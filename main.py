from Scripts import rooms
from Scripts.Entities import player, giant_rat, dragon

pl = player.player()
gr = giant_rat.giant_rat()
dr = dragon.dragon()

rms = {
        0: rooms.start_room(pl),
        1: rooms.room_1(pl),
        2: rooms.room_2(pl),
        3: rooms.room_3(pl),
        4: rooms.room_4(pl)
    }    

def run_game():
    while True:
        # if you win
        if pl.is_winner():
            print("You did it! You beat the game!")
            print("Thanks for playing!")
            return
        # if you die
        elif not pl.is_alive():
            print("You died! Game over!")
            print("Thanks for playing!")
            return
        # if you're still alive
        else:
            # call the current room function
            rms[pl.get_current_room()](pl)
            
            # get input from player
            choice = int(input("What do you do? "))
            
            # while input is not in the range of possible options of the current room
            while choice not in range(0, rooms.num_ops_list[pl.get_current_room()]+1) or not choice.is_integer():
                print("That's not a choice. Try again.")
                choice = int(input("What do you do? "))
            
            # once input is in the range of possible options, print the next message
            print(rooms.chosen_ops_list[pl.get_current_room()][choice+1])
            
            # now need to update the player's current room
            rooms.update_current_room(pl, choice)
            
            # update dictionaries
            rooms.update_ops_list(pl)
            rooms.update_chosen_ops_list(pl)