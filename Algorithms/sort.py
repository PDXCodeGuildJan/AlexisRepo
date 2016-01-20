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

    
    

#sorted_list = selection_sort(test)
#print("Sorted: ", sorted_list)

# BUBBLE SORT
# Given a list of items:
# - Start at the beginning
# - Compare every adjacent pair, swap their position if they are not in the right order (the latter one is smaller
    # than the former one)
# - Every iteration of the list requires one less check, as larger items naturally "sink" to the bottom and smaller
# items "bubble to the top"

def bubble_sort(unsorted_list):

# Description:
# 1. Find the start of the unsorted list

    # 2. Determine if the number at the current position is less than or greater than the number adjacent to it

    # 3. If it is greater than the adjacent number, swap the two numbers' positions
    # - if it is less than, the numbers maintain their positions

    # 4. Increment current position. 

    # 5. Repeat previous three steps until reaching the position in which there are no following
    # numbers to compare

    # 6. Stop when you reach the end of the unsorted list. 

# 7. Repeat this value comparison process through the rest of the list again, excluding whatever is in 
# now sorted end of the list. You will repeat this process until the start is the only remaining position, 
# meaning there are no more positions to compare

# 8. Return the newly sorted list
# End of Description--------------------------------------------------------------------------------------

    print("Unsorted: ", unsorted_list)
# Outer Loop:
# 1. Find the start of the unsorted list
    start = 0 # created variable to establish start

    maxIndex = len(unsorted_list) # created variable that equals index length

# 7. Repeat this value comparison process through the rest of the list again, excluding whatever is in
# the now sorted end of the list. You will repeat this process until the start if the only remaining
# position, meaning there are no more positions to compare
    while maxIndex > start: # function will loop through until the maxIndex reaches 0 (start), which is when
# there will be nothing left to compare

    # inner while loop
    # 2. Determine if the number at the current position is less than or greater than the number adjacent to it
    

    # 5. Repeat previous three steps until reaching the position in which there are no following
    # numbers to compare
        currentIndex = start
        while currentIndex < maxIndex - 1:
    
            if unsorted_list[currentIndex] > unsorted_list[currentIndex + 1]:
        
                temp = unsorted_list[currentIndex]
                unsorted_list[currentIndex] = unsorted_list[currentIndex + 1]
                unsorted_list[currentIndex + 1] = temp

            currentIndex += 1


        maxIndex -= 1 # redefined maxIndex to have it incrementally decrease each time function loops

    return unsorted_list

    

# def swap(the_list, index_a, index_b):

#     # Swaps two items in a list.
#     # Returns: the list with things swapped

#     # 1. Select two items from a given list
#     # 2. Swap the position of the first item with the position of the second item
#     # 3. Return the newly ordered list

#     # Make a temp to hold one value
#     the_list[index_a], the_list[index_b] = the_list[index_b], the_list[index_a]
#     temp = the_list[index_a]

#     # Swap the value
#     the_list[index_a] = the_list[index_b]
#     the_list[index_b] = temp

#     # Return the list with swapped items
#     return the_list

# def insertion_sort(the_list):
#     """Sort the list using the insertion algorithm."""

#     for start_index, value in enumerate(the_list):

#         # Make a temp variable fr the index of the thing we're currently sorting
#         lost_index = start_index
#         lost_value = value

#         # Look for where the lost index's value belongs
#         while (the_list[lost_index] < the_list[lost_index - 1] and lost_index > 0):
#             pass 


if __name__ == "__main__":
    
    test = [4, 68, 57, 19, 3, 40, 97, 31, 44, 68, 20]
    sorted_list = bubble_sort(test)
    print("Sorted: ", sorted_list)








     







