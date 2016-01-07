# Make a madlib that prompts the user for 5 words/phrases
# and then adds those to a silly story.

madlib = "In the early 1900s, crossword "

plural_noun = input("Please give a plural noun: ")

madlib = madlib + plural_noun + " only appeared in children's books. "

adjective = input("Please give an adjective, and if you could capitalize the first letter, that would be nice: ")

madlib = madlib + adjective + " kinkajous first created these marvels. "

#They were often considered (adjective2) in those days. Nonetheless, they were quite popular among (pluralnoun2). Today, (person) is a strong proponent of implimenting such practices in (place)

adjective2 = input("Please give an adjective: ")

madlib = madlib + "They were often considered " + adjective2 + " in those days. "

plural_noun2 = input("Please give a plural noun: ")

madlib = madlib + "Nonetheless, they were quite popular among " + plural_noun2 + ". "

person = input("Please name a person: ")

place = input("Please name a place: ")

madlib = madlib + "Today, " + person + " is a strong proponent of implimenting such practices in " + place + "."


print(madlib)