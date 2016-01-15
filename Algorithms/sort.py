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

	print("Unsorted: ", unsorted_list)
	# find the start of the unsorted list [loop]
	first_num = 0  # assigns variable to first index in unsorted_list - will keep track of the index 
	# through the function based on its assigned value, which is technically just a value, not the index itself,
	# although it will be used to help denote the index throughout the function
	
	# repeat until unsorted list is empty
	while first_num < len(unsorted_list):
		# find the smallest number in the unsorted list
		# make the computer look at every item in the list and find the smallest one
		currentIndex = first_num # whichever index we are currently at and the vantage point from which we are
		# comparing the rest of the list
		currentLowestIndex = first_num # the place for whichever number is the smallest thus far
		while currentIndex < len(unsorted_list): # loops through whatever remaining list there is
			if unsorted_list[currentIndex] < unsorted_list[currentLowestIndex]: # specifies the number the index
			# represents rather than the index itself, so if the number at the current index is less than
			# current lowest number, then this will happen:
				currentLowestIndex = currentIndex # whatever the 
				#currentLowestIndex is becomes the currentIndex
			currentIndex += 1 #currentIndex is redefined by adding 1 to its current value so that when
			# it loops back through, it will move through the list to the next index until it goes through
			# the whole list, which is specified with the initial while loop 

		# Swap the first number and the smallest number in the unsorted list
		# create temporary variable to store what is being swapped so it doesn't disappear during the swap
		temp = unsorted_list[currentLowestIndex]
		unsorted_list[currentLowestIndex] = unsorted_list[first_num]
		unsorted_list[first_num] = temp

		
		

		# update unsorted list with the next number as the first number in the list now
		first_num += 1
		

	return unsorted_list 

	
test = [4, 68, 57, 19, 3, 40]

sorted_list = selection_sort(test)
print("Sorted: ", sorted_list)

# Bubble Sort
# Given a list of items:
# - start at the beginning
# - compare every adjacent pair, swap their position if they are not in the right norder
	 







