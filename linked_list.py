""" Linked List, insert description here """

__author__ = "Alexis Bird"

class Node:
	""" insert description """

	def __init__(self, value):

		self.value = value
		self.next_node = None

	def __str__(self):

		return str(self.value)


class Linked_list:
	""" insert description """

	def __init__(self):

		self.head = None

	def search(self):

		#if??
		pass


	def add(self, value):
		#create a new node
		# give a value for new node?
		# link the most recent nod
		
		new_node = Node(value)
		if self.head == None:
			self.head = new_node
		else:

			whatever_node = self.head

			while whatever_node.next_node != None:
				whatever_node = whatever_node.next_node

			whatever_node.next_node = new_node

	def remove(self, value):

		pass

	def __str__(self):

		stringified_list = ""

		whatever_node = self.head

		while whatever_node.next_node != None:
			stringified_list += str(whatever_node.value) + "; "

			whatever_node = whatever_node.next_node

		if whatever_node.next_node == None:
			stringified_list += str(whatever_node.value)

		return stringified_list

