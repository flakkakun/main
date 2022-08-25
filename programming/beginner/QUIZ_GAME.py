print("welcome to my computer quiz")

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay lets play!")

score = 0 

answer = input("what does cpu stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')


answer = input("what does llc stand for? ")
if answer.lower() == "limited liability company":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')


answer = input("what does seo stand for? ")
if answer.lower() == "search engine optimization":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')


answer = input("what is my name? ")
if answer == "karim":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')
print('you got ' + str(score) + ' questions correct!')

