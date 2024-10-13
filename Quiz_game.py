print("-----QUIZ GAME------")
print("\n")
print("Welcome to the quiz game!")


playing = input("Do you want to play? [Yes/No] ")

if playing.lower() != "yes":
    print("Okay, Goodbye! Game Exited! ")
    print("\n")
    quit()
    
print("Okay, Let's play! ")
print("\n")
print("A few personal details before we start the game! \n Name \n Age \nGender")

agree = input("Do you agree to provide the above details? [Yes/No] ")

if agree.lower() != "yes":
    print("Okay, Goodbye! Game Exited! ")
    print("\n")
    quit()

if agree.lower() == "yes":
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: [Male / Female / Other..] ")
    print("\n")
    print("Your Details are: \n" + "Name: " + name + "\n" + "Age: " + str(age) + "\n" + "Gender: " + gender)

print("\n")
print("Let's get started! ")
print("\n")

answer = input("What's the capital of France? ")
if answer.lower() == "paris":
    print("Correct! ")
else:
    print("Incorrect! ")
    

print("\n")
print("Next Question! ")
print("\n")

answer = input("What's the full meaning of CPU? ")
if answer.lower() == "Central Processing Unit":
    print("Correct! ")
else:
    print("Incorrect! ")




#print("Hello", name, "Welcome to the quiz game!")