# without using buildin function

def find_second_max(arr):
    size = len(arr)
    max1 = max2 = -1
    for i in range(size):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2 and arr[i] < max1:
            max2 = arr[i]
    return max2

print(find_second_max([1, 2, 5, 5, 2, 3,3]))


# with using buildin function
def find_second_max(arr):

    return sorted(list(set(arr)))[-2]

print(find_second_max([1, 2, 5, 5, 2, 3,3]))
