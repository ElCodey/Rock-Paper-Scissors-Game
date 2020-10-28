import random


#Make a small rock-paper-scissors game

#2 player game, that takes inputs for their name and choice
#Best of 5 game
#Checklist for game: Play vs CPU or Player, player names, score counter, 

# Variables for game

game_choices = ["r", "p", "s"]

def player_request():
    #finding out if the user wants to player vs the CPU or another player
    global players
    global p1_name
    global p2_name
    while True:
        try:
            players = int(input("Welcome to Rock/Paper/Scissors. How many players are there? If only one then you will play against the computer."))
        except:
            print("Invalid response, please try again.")
            continue

        
        if players == 1:
            p1_name = input("What is your name? ")
            game_1_player()
            break
        elif players == 2:
            p1_name = input("What is your name Player 1? ")
            p2_name = input("What is your name Player 2? ")
            game_2_player()
            break
        else:
            print("Invalid response, please try again.")
            continue

#Function for one user game
def game_1_player():
    global player_1
    global player_2
    global p1_choice
    global p2_choice

    player_1 = 0
    player_2 = 0

    while player_1 < 3 and player_2 < 3:
        p2_choice = random.choice(game_choices)
        p1_choice = input("Please enter your choice Player 2, r/p/s! ").lower()
        print("Player 1 picked {} and player 2 picked {}!".format(p1_choice, p2_choice))
        rules()
        print("Player 1: {} points || Player 2: {} points.".format(player_1, player_2))
    
#Function for two users
def game_2_player():
    global player_1
    global player_2
    global p1_choice
    global p2_choice
    player_1 = 0
    player_2 = 0

    while player_1 < 3 and player_2 < 3:
        p1_choice = input("Please enter your choice Player 1, r/p/s! ").lower()
        p2_choice = input("Please enter your choice Player 2, r/p/s! ").lower()
        print("Player 1 picked {} and player 2 picked {}!".format(p1_choice, p2_choice))
        rules()
        print("Player 1: {} points || Player 2: {} points.".format(player_1, player_2))
       
        
        


def rules():
    #Rules and points for the game regardless of how many players
    global player_1
    global player_2
    if p1_choice == "r":
        if p2_choice == "s":
            print("Rock beats scissors, player 1 scores a point!")
            player_1 += 1
        elif p2_choice == "p":
            print("Paper beats rock, player 2 scores a point!")
            player_2 += 1
        else:
            print("It's a tie, pick again.")
           
    elif p1_choice == "s":
        if p2_choice == "r":
            print("Rock beats scissors, player 2 scores a point!")
            player_2 += 1
        elif p2_choice == "p":
            print("Scissors beats paper, player 1 scores a point!")
            player_1 += 1
        else:
            print("It's a tie, pick again.")
            
    else:
        if p2_choice == "s":
            print("Scissors beats paper, player 2 scores a point!")
            player_2 += 1
        elif p2_choice == "r":
            print("Paper beats rock, player 1 scores a point!")
            player_1 += 1
        else:
            print("It's a tie, pick again.")
          


#Loop for the game
while True:
    play_game = input("Would you like to play Rock/Paper/Scissors? (Y/N)").lower()
    if play_game not in ["y", "n"]:
        print("Invalid answer, please try again.")
        continue
    elif play_game == "n":
        print("Thanks for playing, goodbye.")
        break
    else:
        player_request()
        if player_1 > player_2:
            print("{} wins!".format(p1_name))
        else:
            try:
                print("{} wins!".format(p2_name))
            except:
                print("Player 2 wins!")

