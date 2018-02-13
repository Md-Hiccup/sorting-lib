import typeSort
import typeSearch

type_of_sort = typeSort.CallSort()
type_of_search = typeSearch.CallSearch()

if __name__ =='__main__':
	inp = input("Enter ur choice\n1- Searching\n2- Sorting\n")
	#print(type(inp))
	if inp == '1':
		opt = input("1- Linear Search\n2- Binary Search\n3- Jump Search\n")
		type_of_search.call(opt)
	elif inp == '2':
		opt = input("1- Bubble Sort\n2- Selection Sort\n3- Insertion Sort\n4- Heap Sort\n5- Quick Sort\n" \
					+"6- Merge Sort\n7- RadixSort\n8- Shell Sort\n9- Comb Sort\n10- Pigeon Hole Sort\n")
		type_of_sort.call(opt)