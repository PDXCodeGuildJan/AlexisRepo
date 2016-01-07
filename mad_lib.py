# Make a madlib that prompts the user for 5 words/phrases
# and then add those to a silly story.

madlib = "In the early 1900s, crossword "

plural_noun = input("Please give a plural noun: ")

madlib += plural_noun + " only appeared in children's books. "

adjective = input("Please give an adjective, and if you could capitalize the first letter, that would be nice: ")

madlib += adjective + " kinkajous first created these marvels. "

adjective2 = input("Please give an adjective: ")

madlib += "They were often considered " + adjective2 + " in those days. "

plural_noun2 = input("Please give a plural noun: ")

madlib += "Nonetheless, they were quite popular among " + plural_noun2 + ". "

person = input("Please name a person: ")

place = input("Please name a place: ")

madlib += "Today, " + person + " is a strong proponent of implimenting such practices in " + place + "."


print(madlib)