import random

Dict = {"snake": 1, "water": -1, "gun": 0}
choice = input("Enter your choice (snake/water/gun): ").lower()

you = Dict[choice]
CompCh = random.choice(["snake", "water", "gun"])
computer = Dict[CompCh]

print(f"You choose {choice}")
print(f"Computer choose {CompCh}")

if computer == you:
    print("Draw")
else:
    if computer == 1 and you == -1:
        print("Computer wins")
    elif computer == -1 and you == 1:
        print("You win")
    elif computer == 0 and you == 1:
        print("Computer wins")
    elif computer == 1 and you == 0:
        print("You win")
    elif computer == 0 and you == -1:
        print("Computer wins")
    else:
        print("You win")
