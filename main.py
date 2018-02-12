import typeSort

type = typeSort.CallSort()

if __name__ =='__main__':
    opt = input("1- Bubble Sort\n2- Selection Sort\n3- Insertion Sort\n4- Heap Sort\n5- Quick Sort\n6- Merge Sort\n" \
    	+ "7- RadixSort\n")
    type.call(opt)
    