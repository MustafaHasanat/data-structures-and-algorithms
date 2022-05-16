def InsertionSort(my_list):
    
    for i in range(1, len(my_list)):
        index = i - 1  
        temp = my_list[i]   

        while index >= 0 and temp < my_list[index]:
            my_list[index+1] = my_list[index]
            index -= 1

        my_list[index+1] = temp
        
    return my_list 


print(InsertionSort([3,2,1]))
 
 