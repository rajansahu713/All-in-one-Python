# Python bin()

def covert_bin(num):
    return bin(num)

convert_to_bin=[1,2,3,4,5,6,7,8,9,10]
coverted_to_bin=[covert_bin(num) for num in convert_to_bin]
print(coverted_to_bin)
binary_num=[num.replace("0b","") for num in coverted_to_bin]
print(binary_num)


