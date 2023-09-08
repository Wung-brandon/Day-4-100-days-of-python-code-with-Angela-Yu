import random

while True:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors:"))

    computer = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.randint(0,2)

    user = computer[computer_choice]
    choice = computer[user_choice]
    #print(user)
    #print(choice)

    if user_choice == computer_choice:
        print(f'Its a draw! Both selected {choice}')
    elif user_choice == 0 and computer_choice == 1 or user_choice == 1 and computer_choice == 2 or user_choice == 2 and computer_choice == 0:
        print(f'You lose! computer choosed {user} and you choosed {choice}')
    elif user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1 or user_choice == 0 and computer_choice == 2:
        print(f'You win! you choosed {choice} and computer choosed {user}')
    #else:
     #   print("Invalid choice")
    play_again = input("Do you want to play again? Type 'Y' or 'N': ").lower()
    if play_again == 'n':
        break
    

