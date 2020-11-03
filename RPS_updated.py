import random

# Function asking for numbers of  players, 2 maximum and returns an int



def player_request():
    try:
        number_players = int(input("How many players are there? (2 maximum)"))
        if number_players == 1 or number_players == 2:
            return number_players
        else:
            print("Invalid number of players.")
            player_request()

    except ValueError:
        print("Invalid number of players.")
        player_request()


# Ask user how many games they want to play


def games():
    try:
        number_games = int(input("How many games do you want to play to?"))
        return number_games
    except ValueError:
        print("Invalid number of games, please try again.")
        games()

# Function to decide winner


def win_checker(p1_choice, p2_choice):
    if ((p1_choice == "r" and p2_choice == "s") or
        (p1_choice == "s" and p2_choice == "p") or
        (p1_choice == "p" and p2_choice == "r")):

       return 1

    elif ((p1_choice == "r" and p2_choice == "p") or
          (p1_choice == "s" and p2_choice == "r") or
          (p1_choice == "p" and p2_choice == "s")):

        return 2
    
    else:
        return 3


# Get user pick
def user_choice():
    choice = input("Please enter your choice (r/p/s): ").lower()
    if choice in ["r", "p", "s"]:
        return choice
    else:
        print("Invalid choice, please try again.")
        user_choice()


def computer_turn():
    return random.choice(["r", "p", "s"])


# Function for one player mode
def one_player():
    # user picks their choice
    user_turn = user_choice()
    computer_pick = computer_turn()
    print("User picks {} and computer picks {}.".format(
        user_turn, computer_pick))
    # Returns winner as 1,2 or 3 (tie)
    return win_checker(user_turn, computer_pick)

# Function for two player mode


def two_player():
    print("Player 1 to pick first.")
    p1 = user_choice()
    print("Player 2 to pick next.")
    p2 = user_choice()
    # Returns winner as 1,2 or 3 (tie)
    return win_checker(p1, p2)


def game():
    # Use function to ask number of players
    players = player_request()
    # Score tracker variables
    player_1_score = 0
    player_2_score = 0

    # Ask number of games
    num_games = games()

    while player_1_score < num_games and player_2_score < num_games:
        #Adding a seperator
        print("--------------------------------------------------")
        print("Player 1 has {} points and Player 2 has {} points.".format(
              player_1_score, player_2_score))
    # One player game
        if players == 1:
            result = one_player()
            # To decide who scores a point
            if result == 1:
                print("Player one scores a point!")
                player_1_score += 1
            elif result == 2:
                print("Player two scores a point!")
                player_2_score += 1
            else:
                print("It's a tie!")
    # 2 player game
        else:
            result_two_player = two_player()
            # To decide who scores a point
            if result_two_player == 1:
                print("Player one scores a point!")
                player_1_score += 1
            elif result_two_player == 2:
                print("Player two scores a point!")
                player_2_score += 1
            else:
                print("It's a tie!")

    return [player_1_score, player_2_score]


def display_results(scores):
    if scores[0] > scores[1]:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


# Program start
if __name__ == '__main__':
    result = game()
    display_results(result)
    print("Thanks for playing.")
