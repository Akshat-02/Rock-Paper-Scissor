rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random as r

choice = int(input("""Welcome to Rock, paper, scissor game.
What do you choose?\n0 for rock, 1 for paper and 2 for scissors :"""))

if choice == 0:
    print("\nYou chose: ")
    print(rock)
elif choice == 1:
    print("\nYou chose: ")
    print(paper)
elif choice == 2:
    print("\nYou chose: ")
    print(scissors)
else:
    print("Enter only from given values :)")

comp_choice = r.randint(0,2)

if choice == 0 or choice == 1 or choice == 2:

    print("Computer chose: ")

    if comp_choice == 0:
        print(rock)
    elif comp_choice == 1:
        print(paper)
    elif comp_choice == 2:
        print(scissors)

    if choice == comp_choice:
        print("It's a draw")
    elif choice == 0 and comp_choice == 2:
        print("You win!!")
    elif choice == 1 and comp_choice == 0:
        print("You win!!")
    elif choice == 2 and comp_choice == 1:
        print("You win!!")
    else:
        print("You loose!! Better luck next time.")

