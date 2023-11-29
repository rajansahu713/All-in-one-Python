import re

def is_valid_indian_mobile(mobile):
    """
    The function `is_valid_indian_mobile` checks if a given mobile number is a valid Indian mobile
    number.
    
    :param mobile: The mobile parameter is a string representing an Indian mobile number
    :return: a boolean value indicating whether the given mobile number is valid or not.
    """
  # The `regex` variable is a regular expression pattern that is used to validate Indian mobile
  # numbers.
    regex = r"^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[6789]\d{9}$"
    return bool(re.match(regex, mobile))

print(is_valid_indian_mobile("919876543210")) # True
print(is_valid_indian_mobile("+919876543210")) # True 
print(is_valid_indian_mobile("079876543210")) # True
print(is_valid_indian_mobile("9876543210")) # True
print(is_valid_indian_mobile("8987654321")) # True
print(is_valid_indian_mobile("98765432100")) # False - 11 digits 