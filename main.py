from Scripts import player, rooms

pl = player.Player()

rms = {
        0: rooms.start_room(pl),
        1: rooms.room_1(pl),
        2: rooms.room_2(pl),
        3: rooms.room_3(pl),
        4: rooms.room_4(pl)
    }

def run_game():
    while True:
        if pl.is_alive():
            rms[pl.get_current_room()]
            choice = int(input("What do you do?\n"))
            if choice in rms[pl.get_current_room()].options:
                rms[pl.get_current_room()].options[choice]
            else:
                print("Invalid choice.")                
        else:
            print("You have died!")
            print("Game over!")
            return