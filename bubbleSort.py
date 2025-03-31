def bubbleSort(arr):
    for i in range(len(arr)-1):
        swapped = False;
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
               arr[j],arr[j+1] = arr[j+1],arr[j]
               swapped = True
        if(not swapped):
            return
        
arr = [int(x) for x in input("enter numbers:").split()]
bubbleSort(arr)
print("Sorted array:")
print(arr)



