class SearchMethod:

	def linear(self, arr, x):
		for i in range(len(arr)):
			if arr[i]  == x:
				return i
		return -1

	def binary(self, arr, low, high, x):
		while low <= high:
			mid = (low + high)//2

			if arr[mid] == x:
				return mid
			elif arr[mid] < x:
				low = mid+1
			else:
				high = mid-1
		return -1