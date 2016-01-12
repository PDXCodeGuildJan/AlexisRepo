#hangman.py
# A program about hanging people if you don't spell things correctly.

from random import randint # when you call randint, it expects two things: randint(to, from) - will randomly
# return a number between those two numbers or either of those two numbers (randint function includes them
# in the range)

words = ["kleptomaniac", "oligarchy", "apocalypse", "kinkajou", "papoose", "lackadaisical", "pedantic"]
numWrong = 0 # do I need to change this?
listedWord = [None] # do I need to change this?

# A function that starts and plays the hangperson game.
# Users can be wrong a maximum of 5 times before they lose,
# the 6th wrong guess triggering Game Over.
def hangperson():
   global listedWord

   # Greet the user
   print("Let's play a game of Hangperson! (And yes, we are so politically correct here that we named the game Hangperson.)")

   # Randomly select a word from the list of words:

   # 1. fine length of word array
   list_length = len(words) # how many words are in the "words" list

   # 2. randomly pick an index from the word array using that length
   rand_index = randint(0, list_length - 1) # pulls a random index number from the list. The "to" is 0 because
   # the list count starts at 0 and the "from" is the list_length - 1 because otherwise there would be no index
   # for the number the total list_length gives since the count starts at 0

   # 3. use that random index to actually get the word out
   chosenWord = words[rand_index] # creates a variable for the randomly chosen word for that round of the game

   # Make the randomly selected word into a list object # convert from string into a list, "cast"?
   listedWord = list(chosenWord) # take the string (in this case, chosenWord) and makes it into 
   # a list of its characters


   # Make another list the same length as the word, but with
   # '_' instead of letters. This will track the user's progress.
   # Use the variable name currentState
   
   # 1. calculate length of the list "listedWord"
   # 2. create second list with "_"s in place of letters, must be same length as listedWord
   blankWord = "_" * len(listedWord)

   # convert blankWord (which is a string) into a list (currentState)
   currentState = list(blankWord)

   # Print the initial state of the game
   printHangperson(currentState)

   # Start the game! Loop until the user either wins or loses
   while currentState != listedWord and numWrong < 6:

      # first, ask the user to guess
      guess = userGuess()

      # see if the guess is in the word, update accordingly
      currentState = updateState(guess, currentState)

      printHangperson(currentState)

   # Determine if the user won or lost, and then tell them accordingly
   if numWrong == 6:
      print("You get nothing! You lose! Good day, sir! (or madame, seeing as we're being politically correct and all)")
   elif listedWord == currentState:
      print("Congratulations, you win!!! Thanks for playing!")
      



# Update the state of the game based on the user's guess.
#
# guess: a character guessed by the user
# currentState: the current state of the word/game
#
# return currentState
def updateState(guess, currentState):
   global numWrong

   # First, determine if the letter guessed is in the word.
   numInWord = listedWord.count(guess)

   # If it isn't, tell the user and update the numWrong var
   
   if numInWord == 0: #means letter is wrong, so we update numWrong:
      numWrong = numWrong + 1 #short hand: numWrong += 1 (can also do with subtraction and multiplication)
      print("Wrong! That noose is feeling a little tighter...")
   # If it is, congratulate them and update the state of the game.
   #    To update the state, make sure to replace ALL the '_' with
   #    the guessed letter.
   elif numInWord > 0: # means letter is in the word
      print("Correct! Yay! There are " + str(numInWord) + " of the letter " + guess + ". Maybe you won't be hanged today after all!")
      # fix grammar
      # while we still have letters to find, keep looping
      numFound = 0
      index = 0
      while numFound < numInWord and index < len(listedWord): # "and" because both conditions must be true to stop looping
         # see if letter is in word at index
         if listedWord[index] == guess: # if at the first index the same thing is stored as the guess...
            currentState[index] = guess
            numFound += 1 # same as numFound = numFound + 1

         index  += 1



   return currentState


# This helpful function prompts the user for a guess,
# accepting only single letters.
# extra credit: check if input is a number and respond accordingly to input
# returns a letter
def userGuess():
   guess = input("Guess a letter in the word! (Type 'exit' to stop playing at any time). ")

   while len(guess) != 1:
      # user has given us too long of a response

      # check if it is "exit", then exit if it is (eliminate case sensitivity)
      if guess == "exit": 
         exit()
      else:
         guess = input("Aaahhh! Too many letters!! Please guess a letter in the word: ") # had to update guess definition
   
      # otherwise, ask them to guess again

   return guess

################# DO NOT EDIT BELOW THIS LINE ##################

# A helpful function to print the hangman.
# DO NOT CHANGE
#
# state: current state of the word
def printHangperson(state):
   person = [" O "," | \n | ", "\| \n | ", "\|/\n | ", "\|/\n | \n/  ", "\|/\n | \n/ \\"]
   print()

   if numWrong > 0:
      print(person[0])

   if numWrong > 1:
      print(person[numWrong-1])

   print("\n\n")

   for i in state:
      print(i, end=" ")

   print("\n")

# This line runs the program on import of the module
hangperson()
