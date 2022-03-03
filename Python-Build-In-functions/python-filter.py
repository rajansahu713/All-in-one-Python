# python Filter

def even_numbers(numbers):
    return numbers if numbers % 2 == 0 else None

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_list = list(filter(even_numbers, number_list))
print("Without lambda function: ",even_numbers_list)

## using lambda function    
even_numbers_list = list(filter(lambda numbers: numbers % 2 == 0, number_list))
print("With Lambda fuction: ",even_numbers_list)


