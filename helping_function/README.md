import re

def validate_email(email):
  """
  Validate email address matching regex pattern.
  """

  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

  if re.fullmatch(regex, email):
    return True
  
  return False
