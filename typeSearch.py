import search

se = search.SearchMethod()

class CallSearch:

	def linearSearch(self):
		array= self.insertArray()
		print("Array are:\t"+str(array))
		print("Linear Searching:\t")
		x = self.searchElement()
		print("Searchin Element: "+str(x))
		i = se.linear(array, x)
		self.chkFound(i)

	def binarySearch(self):
		array = self.insertArray()
		print("Array are:\t"+str(array))
		print("Binary Searching:\t")
		x = self.searchElement()
		print("Searchin Element: "+str(x))
		i = se.binary(array, 0, len(array)-1, x)
		self.chkFound(i)

	inp = {
		1 : linearSearch,
		2 : binarySearch,
		#3 : jumpSearch,
		#4 : interpolationSearch,
	}

	def call(self, inputChoice):
		print("calling..."+inputChoice)
		choice = int(inputChoice)
		self.inp[choice](self)

	def insertArray(self):
		#size = int(input("Enter the size of an array: "))
		#arr = [8, 4, 1, 3, -44, 23, -6, 28, 0]
		arr = [3, 9, 27, 38, 43, 71, 82, 91]
		#for i in range(size):
			#s = int(input())
			#arr.append(s)
		return arr

	def searchElement(self):
		#n = int(input("Enter the Element to search\n"))
		n = 82
		return n

	def chkFound(self, i):
		if i != -1:
			print("Element Found at index:  "+str(i))
		else :
			print("Element is not present")
