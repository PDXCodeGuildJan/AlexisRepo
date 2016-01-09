# Create a text based maze. It must have 5 rooms, including the start and finish, and handle incorrect inputs gracefully. Also, you should be able to exit at any time.



# When the program first opens, welcome the player to the maze: "Welcome to the Maze! Good luck and enjoy the adventure. Type 'exit' to leave at any point."

# Program exits when user types "exit," capitalization does not matter. 

# User starts in the White Room: "You are in a purely white, empty room with padding on the walls, much like an insane asylum, except there are two doors, east and west.
#Which door do you choose?"

#User types "east" or "west" to go into a different room. Make sure capitalization isn't issue with "east" or "west." If anything other than "east" or west"
# is typed, print: "I'm sorry, but I didn't understand that. Which door do you choose?"

#User types "west" : The West door leads to the Dark Room: "You are in complete darkness. You can't see anything except for a sliver of light to go back. Which way do you go?"
# if user types, "back" (capitalization doesn't matter), back in White Room.
# The East door leads to the Furry Room: "You are in a small room, completely covered in soft furriness. There are three doors: north, south, and east.
# Which way do you go?"
# if user types "north," goes into Flying Spaghetti Monster room: "You enter this room and...there's a giant Flying Spaghetti Monster that's about to eat you!
#Maybe you should go back... Which way do you go?"
# if user types, "back", return to Furry Room, otherwise, print "I'm sorry, but I didn't understand that. Which way do you wanto go?"
# From furry room, if user types "east", goes into Quick Sand room: "It looks like you're about to step into quick sand. Which way would you like to go?"
# if user types "back", go back to Furry Room. Otherwise, print "I'm sorry, but I didn't understand that. Which way do you wanto go?"
# From furry room, if user types "south", finishes maze, print "Congratulations! You made it through the maze! Would you like to go through again?"
# if user types "yes", print welcome slogan again and begin in White Room. if user types no, print "Thanks for playing. Goodbye!" and then exit the program. if user types anything else, print
# "I'm sorry, I didn't understand that. Yes or no?" - make sure "yes" and "no" are not case sensitive

def main():
	welcome = ("Welcome to the Maze! Good luck and enjoy the adventure."
			" Type 'exit' to leave the Maze at any point. You are in a purely white,"
			" empty room with padding on the walls, much like an insane asylum. "
			"But, lucky for you, there are two doors: east and west. ")
	print(welcome)

	entry = ""

	 #add no case sensitivity
	while entry != "exit" or "east" or "west":
		entry = input("Which door do you choose? " )

		if entry == "exit": #add no case sensitivity
			exit()
		elif entry == "west": #add no case sensitivity
			print("right") # execute function for Dark Room
		elif entry == "east": #add no case sensitivity
			print("wrong")# execute function for Furry Room
		else:
			print("I'm sorry, but I didn't understand that.")

main()

def dark_room():
	print("You are in complete darkness. You can't see anything except for a sliver of light to go back. ")

