def InsertionSort(my_list):
    
    for i in range(1, len(my_list)):
        index = i - 1  
        temp = my_list[i]   

        while index >= 0 and temp < my_list[index]:
            my_list[index+1] = my_list[index]
            index -= 1

        my_list[index+1] = temp
        
    return my_list 


def Mergesort(arr):
    n = len(arr)

    if n > 1:
      mid = n//2  
      left = arr[:mid]  
      right = arr[mid:] 
      
      Mergesort(left)
      Mergesort(right)
      Merge(left, right, arr) 
      
      return arr


def Merge(left, right, arr): 
    i, j, k = 0, 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else: 
            arr[k] = right[j]
            j += 1

        k += 1
        
    if i == len(left): 
        for element in right[j:]:
            arr[k] = element
            k += 1
    else:
        for element in left[i:]: 
            arr[k] = element
            k += 1
        

def QuickSort(arr, left, right):
    if left < right:
        position = Partition(arr, left, right)
        QuickSort(arr, left, position - 1)
        QuickSort(arr, position + 1, right)
        
    return arr


def Partition(arr, left, right):
    pivot = arr[right]
    low = left - 1
    for i in range(left, right):
        if arr[i] <= pivot:
            low += 1
            Swap(arr, i, low)

    Swap(arr, right, low + 1)
    return low + 1

def Swap(arr, i, low):
    temp =  arr[i]
    arr[i] = arr[low]
    arr[low] = temp

    
if __name__ == "__main__":
    print(QuickSort([8,4,23,42,16,15], 0, 5))
 
  