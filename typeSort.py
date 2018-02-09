import sort 

s = sort.SortMethod()

class CallSort:

    def bubbleSort(self):
        array = self.insertArray()
        print("BubbleSort")
        print("Unsorted Array:\t"+str(array))
        s.bubble(array)
        print("Sorted Array:\t"+str(array))        

    def selectionSort(self):
        array = self.insertArray()
        print("SelectionSort")
        print("Unsorted Array:\t"+str(array))
        s.selection(array)
        print("Unsorted Array:\t"+str(array))

    def insertionSort(self):
        array = self.insertArray()
        print("InsertionSort")
        print("Unsorted Array:\t"+str(array))
        s.insertion(array)
        print("Unsorted Array:\t"+str(array))

    def heapSort(self):
        array = self.insertArray()
        print("HeapSort")
        print("Unsorted Array:\t"+str(array))
        s.heap(array)
        print("Sorted Array:\t"+str(array))
        

    def quickSort(self):
        array = self.insertArray()
        print("QuickSort")
        print("Unsorted Array:\t"+str(array))
        s.quick(array, 0, (len(array)-1))
        print("Sorted Array:\t"+str(array))


    def mergeSorting(self):
        array = self.insertArray()
        print("MergeSort")
        print("Unsorted Array:\t"+str(array))
        s.mergeSort(array, 0, (len(array)-1))
        print("Sorted Array:\t"+str(array))
    
    inp = {
        1 : bubbleSort,
        2 : selectionSort,
        3 : insertionSort,
        4 : heapSort,
        5 : quickSort,
        6 : mergeSorting,
    }

    def call(self,inputChoice):
        print("calling... "+ inputChoice)
        choice = int(inputChoice);
        self.inp[choice](self)

    def insertArray(self):
        #size = int(input("Enter the size of an array: "))
        arr = [64, 25, 12, 22, 11, 32, 33, 21, 55]
        #for i in range(size):
         #   s = int(input())
          #  arr.append(s)
        return arr
