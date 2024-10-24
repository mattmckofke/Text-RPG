from Scripts import rooms
from Scripts.Entities import player, giant_rat, dragon

pl = player.player()
gr = giant_rat.giant_rat()
d = dragon.dragon()

rms = {
        0: rooms.start_room,
        1: rooms.room_1,
        2: lambda: rooms.room_2(gr),
        3: rooms.room_3,
        4: lambda: rooms.room_4(pl),
        5: rooms.end_room
    }    

def run_game():
    # while player is not winner and player is alive
    while not pl.is_winner() and pl.is_alive():
        rms[pl.current_room]()
        
        # try to get a choice from the player
        try:
            choice = int(input("What do you do? "))
            if choice not in rooms.ops_list:
                raise ValueError
        except ValueError:
            print("That's not a choice. Try again.")
            continue
        
        # update dictionaries
        rooms.update_ops_list(pl, gr, d)
        rooms.update_chosen_ops_list(pl, gr, d)
        
        rooms.update_current_room(pl, choice)

run_game()