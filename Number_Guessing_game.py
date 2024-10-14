import random


top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    print("The number you typed is: ",top_of_range)
    if top_of_range <= 0:
            print("Type a number that is greater than 0 next time!!")
            quit()
   
else:
    print("Type a number next time :) ")
    quit()
    
random_number = random.randint(0,top_of_range)
# print("Your Random is: ",random_number)

guesses = 0

while True:
    user_guess = input("Make a guess: ")
    guesses += 1
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
   
    else:
        print("Type a number next time :) ")
        continue
    
    if user_guess == random_number:
        print("You got it right!!!")
        
        break
    else:
        if user_guess > random_number:
            print("Your guess was above the number!! Try again :)")
        else:
            print("Your guess was below the number!! Try again :)")


print(f"You got it right in {guesses} guesses")