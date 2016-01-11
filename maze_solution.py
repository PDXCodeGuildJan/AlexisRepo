def main():
	
	current_room = start

	while current_room != finish:
		new_room = current_room()
		current_room = new_room

	#Call finish
	current_room()


def start():
	print("You find yourself in a maze. Exits are East and South. Can you escape?")


	invalidmove = True

	while invalidmove:
		move = input("Would you like to go east or south?")

		move = move.lower()

		if move == "east":
			invalidmove = False
			return room1
		elif move == "south":
			invalidmove = False
			return room3
		elif move == "q":
			print("Fine then, Goodbye!")
			exit()
		else:
			print("I'm sorry, I didn't understand. Please enter East or South. ")

