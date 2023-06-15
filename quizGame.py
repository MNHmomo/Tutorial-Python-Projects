print("Welcome to my I.T. quiz!")
text = "MACHIAVELLIAN"
print(text.lower())

playing = input("Would you like to start? ")

print(playing)

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :) ")

score = 0

answer = input("What deos CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Sorry, but that is incorrect.")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Sorry, but that is incorrect.")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Sorry, but that is incorrect.")

answer = input("What does IT stand for? ")
if answer.lower() == "information technology":
    print("Correct!")
    score += 1
else:
    print("Sorry, but that is incorrect.")

print("You got " + str(score) + " questions correct.")
print("You got " + str((score/4) * 100) + "%")
