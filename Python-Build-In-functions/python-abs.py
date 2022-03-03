# Python abs()

# if the result is negative, it will be converted to positive
def multiply(a, b):
    return abs(a * b)

mul_list =[(1,3),(-2,4),(3,-5)]
multiply_abs = [multiply(a,b) for a,b in mul_list]
print(multiply_abs)

#If number is complex number, it will return the magnitude
def complex_abs(complex_num):
    return abs(complex_num)

complex_list=[(1+2j),(-2+3j),(3-4j)]
complex_abs = [complex_abs(complex_num) for complex_num in complex_list]
print(complex_abs)

    

