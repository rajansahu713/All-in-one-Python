def bubbleSort(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)-i):
            #print(array[i], array[j])
            if array[i] > array[j]:
                array[i] , array[j] = array[j], array[i]
        print(array[i])


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)