import urllib.parse

def urlencode(str):
  return urllib.parse.quote(str)


def urldecode(str):
  return urllib.parse.unquote(str)

str = '{"id": "23423dsfsf34fds343v", "params": ["param1","param2","param3"]}'
encoded = urlencode(str)
print(encoded)  # '%7B%22name%22%3A%20%22Kinkin%22%7D'
decoded = urldecode(encoded)
print(decoded)  # '{"name": "Kinkin"}'