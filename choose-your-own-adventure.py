name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You're on a dirt road that has come to an end, and you have the option of turning left or right. Which path do you want to take? ")

if answer == "left":
    answer = input("When you arrive to a river, can you walk around it or swim across it? Type walk to stroll around and swim to swim across to get started: ")

    if answer == "swim":
        print("You swam over only to get devoured by an alligator.")
    elif answer == "walk":
        print("You went for miles, ran out of water, and lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input("You come to a bridge that appears to be shaky; do you wish to cross it or return (cross/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        print("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you LOSE.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose. ')

print("Thank you for trying", name)