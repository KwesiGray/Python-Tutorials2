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


name.upper()
gender.upper()
score = 0
Q_no = 0



print("\n")
print("Let's get started! ")
print("\n")

Q_no += 1
answer = input(f"{Q_no}. What's the capital of France? ")
if answer.lower() == "paris":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")
    
    

print("\n")
print("Next Question! ")
print("\n")

Q_no += 1
answer = input(f"{Q_no}. What's the full meaning of CPU? ")
if answer.lower() == "central processing unit":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")
    
    
    

print("\n")
print("Next Question! ")
print("\n")
Q_no += 1
answer = input(f"{Q_no}. What is the capital of Ghana? ")
if answer.lower() == "accra":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")
    
    



print("\n")
print("Next Question! ")
print("\n")
Q_no += 1
answer = input(f"{Q_no}. What's the largest organ in the human body? ")
if answer.lower() == "liver":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")
    
    



print("\n")
print("Next Question! ")
print("\n")
Q_no += 1
answer = input(f"{Q_no}. What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")
    
    



print("\n")
print("Next Question! ")
print("\n")
Q_no += 1
answer = input(f"{Q_no}. Sound is measured in what unit? ")
if answer.lower() == "decibels":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")
    
    



print("\n")
print("Next Question! ")
print("\n")
Q_no += 1
answer = input(f"{Q_no}. What is the 5th planet from the sun ")
if answer.lower() == "jupiter":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")


print(f"Your final score is: {score} out of {Q_no}")
f_percent = score/7 * 100
f_percent = round(f_percent)

print(f"Your Percentage Score is: {f_percent}% ")

print(f"Hello {name}, you had {score} as your score. 36% of people with age {age} passed and they are {gender}s.")


#print("Hello", name, "Welcome to the quiz game!")