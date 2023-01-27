#individual assignment done by betelihem andualem id=0341
# import libraries
import random

# declare variable
player_name = input("Enter your name: ")
computer_name = "Computer Player"
player_score = 0
computer_score = 0
ties = 0

# print heading
print("(Rock,Paper and Scissors Game)")
print(" ***************************")

# main game loop
while True:
    # get user input
    print("\nPick one of the following:") 
    print("1. Rock   2. Paper  3. Scissors")
    player_choice = int(input("Enter Your Choice: "))
    
    # validate user input
    if 0 < player_choice < 4:
        if player_choice == 1:
            print("\nYour choice was Rock")
        elif player_choice == 2:
            print("\nYour choice was Paper")
        else:
            print("\nYour choice was Scissors")
                    
        # get computer input
        computer_choice = random.randint(1,3)
        if computer_choice == 1:
            print("\nComputer's choice was Rock")
        elif computer_choice == 2:
            print("\nComputer's choice was Paper")
        else:
            print("\nComputer's choice was Scissors")
            

        # compare player and computer input
        if player_choice == computer_choice:
            print("\nIts a draw")
            ties += 1
        elif (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
            print("\nCongratulation! You have won!")
            player_score += 1
        else:
            print("\nSorry! You lose!")
            computer_score += 1

        # print scores
        print("\nGame scores")
        print(player_name+": "+str(player_score))
        print(computer_name+": "+str(computer_score))
        print("Ties: "+str(ties))

        # check if user wants to play again        
        print("\nDo you want to play again? (yes/no):")
        again = input()  
        if again == "yes":
            continue
        else:
            break;
    else:
        print("\nPlease enter valid choice!")
