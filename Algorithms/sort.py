# Define a function called "selection_sort" that expects a list

# Write an implementation of Selection Sort in this function by Returning it

# Test function: sorted = selection_sort([30, 7, 42]), print(sorted)

# Create a function (sorting algorithm) in which a list of items is sorted in order from smallest to biggest
# If two numbers are the same in the list, your algorithm should be able to handle it

def selection_sort(unsorted_list):
	
	# 1. Loop through list to find the smallest item, then the next smallest item, then the next, etc.
	# so we would look at the first item (index 0) and loop to compare it to the second item - if 
	#second item is smaller than first item, second item would take place of first item (they would swap indexes)
	# but if first item is smaller than second item, they would stay in the same place (maintain their indexes)
	# then we would loop to the next item and compare it to whichever item has been deemed the smallest item
	# thus far (current smallest) - if the next item is smaller than the current smallest item, the next item will
	# take the place of the current smallest item
	# this process will continue until reaching the end of the list
	# the final piece will be to print (return?) a sorted version (smallest to biggest) of the 
	# original unsorted_list 
	

	# Given a random list of numbers, sort said list into numerical order from smallest to biggest: 


	# take the first number in the unsorted list 
	first_number = unsorted_list[0] # assigns variable to first item in unsorted_list
	next_number = unsorted_list[] # can I put a blank index here to denote moving through each index in the list??

	# find the smallest number in the unsorted list
	if first_number > next_number:
	# Swap the first number and the smallest number in the unsorted list

	# update unsorted list with the next number as the first number in the list now

	# repeat until unsorted list is empty
	 







