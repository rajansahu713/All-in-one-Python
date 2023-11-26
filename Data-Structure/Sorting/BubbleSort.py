def bubbleSort(array):
    # for i in range(len(array)):
    #     for j in range(i+1,len(array)):
    #         #print(array[i], array[j])
    #         if array[i] > array[j]:
    #             array[i] , array[j] = array[j], array[i]
    #     print(array[i])
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                

data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)