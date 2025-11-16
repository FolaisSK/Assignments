player_one = input("(Player 1) Enter rock, paper or scissors: ").lower()
player_two = input("(Player 2) Enter rock, paper or scissors: ").lower()

if player_one == player_two:
	print("Tie")
else: 
	if player_one == "rock":
		if player_two == "scissors":
			print("Player 1 wins!")
		else:
			print("Player 2 wins!")

	elif player_one == "paper":
		if player_two == "rock":
			print("Player 1 wins!")
		else:
			print("Player 2 wins!")

	elif player_one == "scissors":
		if player_two == "paper":
			print("Player 1 wins!")
		else:
			print("Player 2 wins!")

