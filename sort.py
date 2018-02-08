import math

class SortMethod:

    #************ Bubble Sort *******************

    def bubble(self, arr):
        #size = len(arr)
        for i in range(len(arr)):
            for j in range(0,len(arr)-i-1):
                if(arr[j]>arr[j+1]):
                    arr[j],arr[j+1] = arr[j+1],arr[j]


    
    #************** Selection Sort ****************
    
    def selection(self, arr):
        # Traverse through all array elements
        for i in range(len(arr)):
            # Find the minimum element in remaining unsorted array
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            # Swap the found minimum element with the first element        
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


    
    #**************** Insertion Sort ******************

    def insertion(self, arr):
        # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):
            key = arr[i]
            # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
            j = i-1
            while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key


    
    #**************** Heap Sort **********************
    
    def heapify(self, arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2
        # See if left child of root exists and is
        # greater than root
        if l < n and arr[i] < arr[l]:
            largest = l
 
        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r
 
        # Change root, if needed
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]  # swap
 
            # Heapify the root.
            self.heapify(arr, n, largest)
            
    def heap(self, arr):
        n = len(arr)
        # Build a maxheap.
        for i in range(int(n/2 -1), -1, -1):
            self.heapify(arr, n, i)
 
        # One by one extract elements
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]   # swap
            self.heapify(arr, i, 0)



    #************* Quick Sort ******************
    
    # This function takes last element as pivot, places the pivot element at its correct position in sorted
    # array, and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot
    def partition(self, arr, low, high):
        pi = arr[high]      # pivot
        i = (low - 1)       # index of smaller element

        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if arr[j] <= pi:
                # increment index of smaller element
                i +=1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1    
    
    # arr[] --> Array to be sorted ,  low --> starting index,  high --> ending index
    def quick(self, arr, low, high):    
        if low < high:
            # pi(pivot) is partitioning index, arr[pi] is at right place
            pi = self.partition(arr, low, high) 
            
            # Separately sort elements before partition and after partition 
            self.quick(arr, low, pi-1)   # before pi 
            self.quick(arr, pi+1, high)  # after pi
        
    
    #************** 

    
    

            