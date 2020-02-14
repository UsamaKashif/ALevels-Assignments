# node of the binary tree
class Node:
	def __init__(self, data):
		self.key = data
		self.left = None
		self.right = None

# creating the binary tree
class BinaryTree:
	def __init__(self,root=None):
		self.root = Node(root)

	# prints the data in the tree
	def printTree(self, traversalType):
		if traversalType == "preorder":
			return self.preOrder(myTree.root, "")
		elif traversalType == "inorder":
			return self.inOrder(myTree.root, "")
		elif traversalType == "postorder":
			return self.PostOrder(myTree.root, "")
		else:
			print("traversalType is not supported")
			return False

	# pre order traversal 
	def preOrder (self,start,traversal):
		# root -> left -> right
		if start:
			traversal += (str(start.key) + ".")
			traversal = self.preOrder(start.left, traversal)
			traversal = self.preOrder(start.right, traversal)

		return traversal

	# finding an item in the tree
	def findItem(self, key):
		found = False
		if self.root.key == key:
			found = True
		else:

			q = []
			q.append(self.root)

			while(len(q)):
				temp = q[0]
				q.pop(0)
				
				if(key > temp.key) and (temp.right != None):
					q.append(temp.right)
					if (temp.right.key == key):
						found = True
					else:
						continue 

				if (key < temp.key) and (temp.left != None):
					q.append(temp.left)
					if temp.left.key == key:
						found = True
					else:
						continue

		if found == True:
			print("Data Found")
		else:
			print("Data not found")



	# in-order traversal 
	def inOrder (self,start,traversal):
		#  left => root -> right
		if start:
			traversal = self.inOrder(start.left, traversal)
			traversal += (str(start.key) + ".")
			traversal = self.inOrder(start.right, traversal)

		return traversal

	# post-order traversal 
	def PostOrder(self,start,traversal):
		# left -> right -> root
		if start:
			traversal = self.PostOrder(start.left, traversal)
			traversal = self.PostOrder(start.right, traversal)
			traversal += (str(start.key) + ".")

		return traversal

	# inserting data in tree
	def insert(self,key):
		#  if the root is empty we insert data at the root
		if self.root.key == None:
			self.root.key = key
		else: # else insert the data in order by looping though the tree

			q = []
			q.append(self.root) #insrting the root in an empty array

			while(len(q)):
				temp = q[0]
				q.pop(0) #removing the first element of array
				if (key > temp.key) and (temp.right == None):  # if the right of a node is empty and the data is greater than the node's data, we place it in the right
					temp.right = Node(key)
					break

				if (key < temp.key) and (temp.left == None): # if the left of a node is empty and the data is smaller than the node's data, we place it in the left
					temp.left = Node(key)
					break
				
				if(key > temp.key) and (temp.right != None):  # if the entered data is greater than the node's data and right of node is not empty, we append that node in the list "q"
					q.append(temp.right)
					continue 

				if (key < temp.key) and (temp.left != None): # if the entered data is smaller than the node's data and left of node is not empty, we append that node in the list "q"
					q.append(temp.left)
					continue




def Menu():
	print("1: Add an Item")
	print("2: Find an Item")
	print("3: Display all  using inorder traversal")
	print("4: Display all  using preorder traversal")
	print("5: Display all  using postorder traversal")
	print("6: Exit")
	choice = int(input("Enter your choice.. "))

	while choice <1 or choice >6:
		print("")
		print("Enter between 1 and 5 (inclusive)")
		choice = int(input("Enter your choice.. "))
		print("")

	return choice


def operation(choice, myTree):
	if choice == 1:
		print("")
	
		data = input("Enter data to insert.. ")
		while data == "":
			print("")
			print("Do not leave blank.. ")
			data = input("Enter data to insert.. ")
			print("")

		try:
			data = int(data)
		except:
			pass
		myTree.insert(data)
		print("")


	elif choice == 2:
		print("")
		data = input("Enter data to find.. ")
		try:	
			data = int(data)
		except:
			pass
		myTree.findItem(data)
		print("")

	elif choice == 3:
		print("")
		print(myTree.printTree("inorder"))
		print("")

	elif choice == 4:
		print("")
		print(myTree.printTree("preorder"))
		print("")
	elif choice == 5:
		print("")
		print(myTree.printTree("postorder"))
		print("")


if __name__ == "__main__":

	myTree = BinaryTree()
	choice = Menu()

	while choice != 6:
		operation(choice, myTree)
		choice = Menu()