import random

computer_wins = 0
user_wins = 0
options = ["rock", "paper", "scissors"] 

while True:
    user_input = input("Type [Rock], [Paper] , [Scissors] or Q to quit: ").lower()
    
    if user_input == "q":
        print("Game exited successfully :)")
        break
    
    
    if user_input not in options:
        continue
    
    #now if the user types any of the 3 words above this should happen
    
    random_number = random.randint(0,2)
    #0=rock, 1=paper, 2=scissors
    
    computer_pick = options[random_number]
    print("Computer Picked:", computer_pick , ".")
    
    

print("GoodBye!!")
        
    
    