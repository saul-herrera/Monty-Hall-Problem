#Created on Sat Mar 12 17:53:51 2022 - https://github.com/saul-herrera
import random as rm
Doors = ["Goat", "Goat", "Car"]
player_switches = False #You can change to True and compare rate of wins
N_trials = 10000
win_counter = 0.
lose_counter = 0.
for i in range(N_trials):
    #All doors closed:
    unpicked_doors = Doors.copy()
    #Player picks door at random:
    players_pick_number = rm.choice(range(len(Doors)))
    players_pick = Doors[players_pick_number]
    unpicked_doors.pop(players_pick_number)    
    #Host reveals a goat:
    unpicked_doors.remove("Goat")   
    #Host offers door change:
    if player_switches:
            players_pick = unpicked_doors[0]
    if players_pick in ["Goat"]:
        lose_counter += 1
    elif players_pick in ["Car"]:
        win_counter += 1
    else: 
        print("There's some error")
print("Player switches doors -> " + str(player_switches))
print("Outcome after playing " + str(N_trials) + " times:\n" 
      "% of wins = " + str(100*win_counter/N_trials)+"%" 
      + "\n% of loses = " + str(100*lose_counter/N_trials)+"%")

    
        
            
