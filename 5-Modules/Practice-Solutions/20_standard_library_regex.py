import re

pattern = r"\d+"
text = "There are 123 apples 456"

match = re.search(pattern, text)
print(match.group())
