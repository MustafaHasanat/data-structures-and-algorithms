def InsertionSort(my_list):
    
    for i in range(1, len(my_list)):
        index = i - 1  
        temp = my_list[i]   

        while index >= 0 and temp < my_list[index]:
            my_list[index+1] = my_list[index]
            index -= 1

        my_list[index+1] = temp
        
    return my_list 


# [0, -5, 1, 4, 8]
def Mergesort(arr):
    n = len(arr)

    if n > 1:
      mid = n//2  # 2
      left = arr[:mid]  # 0, -5
      right = arr[mid:]  # 1, 4, 8
      
      Mergesort(left)
      Mergesort(right)
      Merge(left, right, arr)


def Merge(left, right, arr):  # 0 -5  [0, -5, 1, 4, 8]
    i, j, k = 0, 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1
        

    if i == len(left):  # if there are no more elements in the left list
        for element in right[j:]:
            arr[k] = element
            k += 1

    else:
        for element in left[i:]:     # for each element in the left list
            arr[k] = element
            k += 1
        
    

    
    
    
    
    
if __name__ == "__main__":
    x = [0, -5, 1, 8, 4]
    Mergesort(x)
    print(x)
 
 