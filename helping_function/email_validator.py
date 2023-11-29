import re

def validate_email(email):
    """
    The function `validate_email` checks if a given email address is valid according to a regular
    expression pattern.
    
    :param email: The `email` parameter is a string that represents an email address
    :return: a boolean value. It returns True if the email is valid according to the regular expression
    pattern, and False otherwise.
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.fullmatch(regex, email):
        return True

    return False