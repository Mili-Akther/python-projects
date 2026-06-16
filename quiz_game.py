print('welcome to my computer quiz!')

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print('okay! Lets play :)')
score = 0

answer = input('What does CPU stand for? ')
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input('what does GPU stand for? ')
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input('What does RAM stand for? ')
if answer.lower() == "Random Access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " Questions correct!")
print("You got " + str((score / 3) * 100) + "%.")
