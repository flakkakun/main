name = input("type your name: ")
print("Welcome", name, "to this adventure!")

answer = input('You are on a dirt road, it has come to an end and you can go left or right: ')

if answer == "left" :
    answer = input("You come to a river, you can walk around it or swim across. What do you want to do? Type walk to walk or swim to swim: ")

    if  answer == "swim":
        print('You swam across and were eaten b a crocodile')

    elif answer == "walk":
        print("You walked for many miles and ran out of water and food and lost the game")

    else:
        print("Not a valid option.  You lose.")

elif answer == "right":
    answer = input("You come to a bridge that looks wobbly an now have to choose to either cross, go back or walk around. type the corresponding word for each action to proceed: ")

    if answer == "cross":
        print("You attempt to coss the bridge and barley make it through alive")
        answer = input("As youre walking you meet a stranger, do you want to talk to them (yes/no)")
        if  answer == 'yes':
            print('you talk to the stranger and they give you 200 gold')
        elif answer == "no":
            print('the stranger was offended and you lose')

    elif answer == "walk":
        print('a pack of wolves find and hunt you. You lose.')

    elif  answer == "back":
        print('you tried to head back but forgot the way. you lose')

    else:
        print('not a valid option. you lose')
else:
    print('Not a valid option. You lose.')