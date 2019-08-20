guess = 0

while guess != 5:

	guess = input("Guess a number between 1 and 10: ")

	guess = int(guess)


	if guess == 5:
		print("Your guess was correct.")
		break

	else:
		print("Your guess was incorrect")
