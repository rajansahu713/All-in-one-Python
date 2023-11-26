def merge(list1, list2):
    combine =[]
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combine.append(list1[i])
            i += 1
        else:
            combine.append(list2[j])
            j += 1

    while i < len(list1):
        combine.append(list1[i])
        i += 1

    while j < len(list1):
        combine.append(list2[j])
        j += 1

    return combine

def merge_sort(my_list):
    print(type(my_list))
    if len(my_list) ==1:
        return my_list
    
    mid_index = len(my_list)//2
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)


 
original_list = [3,1,4,2]

sorted = merge_sort(original_list)
print("Original list: ",original_list)
print("After running merge sorted: ",sorted)