print("Welcome to the quiz game!!!!!! :) ")

playing = input("Do you want to play this game?? ")
if playing.lower() !="yes":
    quit()
print("yay! we gonna play it <3 💥")
score = 0

answer = input("What is the full form of CPU? ")
if answer.lower() == "central processing unit":
    print('Correct :)')
    score+=1
else:
    print('Incorrect :|')


answer = input("What is the full form of GPU? ")
if answer.lower() == "graphics processing unit":
    print('Correct :)')
    score+=1
else:
    print('Incorrect :|')


answer = input("What is the full form of RAM? ")
if answer.lower() == "random access memory":
    print('Correct :)')
    score+=1
else:
    print('Incorrect :|')


answer = input("What is the full form of PSU? ")
if answer.lower() == "power supply unit":
    print('Correct :)')
    score+=1
else:
    print('Incorrect :|')


answer = input("What is the full form of B.E? ")
if answer.lower() == "bachelor of engineering":
    print('Correct :)')
    score+=1
else:
    print('Incorrect :|')


print("Your score was " +str(score) +" out of 5  :) ")
print("Your percentage was " +str((score/5)*100) +" 💥💥💥 ")