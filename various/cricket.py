from random import choice
from sys import exit

options = ["It's a four!!!'", "What a corker!", "OUT!!!", "You are at silly mid off!", "My dear old thing, it's the end of the Over!'", "You could have hit that with a rhubarb stick!!"]

def playing_the_ashes():
    counter = 1
    print("""You are at Lord's, choose a number from 1 to 7 to see in what role you play""")
    while counter < 5:
        role = int(input('> '))
        if (role >= 1 and role <= len(options)):
            print(choice(options))
        else:
            print("You cannot count, go rub sugar on the ball!!")
        counter += 1

if __name__ == "__main__":
    exit(playing_the_ashes())
