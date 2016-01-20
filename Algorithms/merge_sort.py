__author__ = "Alexis Bird"

"""Implements the merge sort algorithm, recursively, in Python."""

def main():
	"""Take a random list and use merge_sort to sort it"""

	# Simplest
	unsorted = [4, 7, 14, 2, 94, 38, 2]
	sorted = merge_sort(unsorted)
	print(sorted)



def merge_sort(unsorted):
	"""Implement the merge sort algorithm"""
	# Third Simplest
	length = len(unsorted)
	#	Split the list into two halves, if list length is greater than 1
	if length > 1:

		#	first_sorted = sort the first half using merge_sort
		#	second_sorted = sort the second half using merge_sort
		left = unsorted[:(length // 2)]
		right = unsorted[(length // 2):]

		left = merge_sort(left)
		right = merge_sort(right)
		print("unsorted left: ", left)
		print("unsorted right: ", right)

		#	merge the two sorted halves back together into a merged list
		merged = merge(left, right)
		print("merged list of: ", merged)

		#	return the merged, sorted list
		return merged
	else: 
		return unsorted



def merge(left, right):
	"""Given two lists, merge them together into a third list, which is sorted."""

	# Second Simplest
	temp_list = [] # Create empty list for temporary list. You can also use temp_list = list() to create this
	left_i, right_i = 0, 0 # left index variable equals zero, right index variable equals 0 (tuple)
	left_len, right_len = len(left), len(right)


	while left_i < left_len and right_i < right_len:
		if left[left_i] <= right[right_i]:
			temp_list.append(left[left_i])
			left_i += 1


		elif right[right_i] < left[left_i]: # you could also just put an else instead of the elif and condition
			temp_list.append(right[right_i]) 
			right_i += 1

	

	# Command computer to spit out remainder of one list if the other list ends before it
	if left_i < left_len:
		temp_list.extend(left[left_i:])

	elif right_i < right_len:
		temp_list.extend(right[right_i:])


	return temp_list







if __name__ == "__main__":
	main()