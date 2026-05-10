player_one = input("Player 1, enter Rock, Paper, or Scissors: ").lower()
player_two = input("Player 2, enter Rock, Paper, or Scissors: ").lower()

if player_one == player_two:
    print("Tie")
else:
    if player_one == "rock":
        if player_two == "scissors":
            print("Player 1 wins")
        else:
            print("Player 2 wins")
    elif player_one == "paper":
        if player_two == "rock":
            print("Player 1 wins")
        else:
            print("Player 2 wins")
    elif player_one == "scissors":
        if player_two == "paper":
            print("Player 1 wins")
        else:
            print("Player 2 wins")
    else:
        print("Invalid input from Player 1")

