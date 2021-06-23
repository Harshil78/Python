import re

str = "how are you.how is everthing"
matches = re.findall("e.?e", str)  # e.*e,how
print(matches)
matches = re.search("how", str)  # e.*e,how
print(matches)
print(matches.span())
print(matches.group())
print(matches.string)
matches = re.split(" ", str)  # e.*e,how
print(matches)
print(re.sub(" ", ",", str))
str = "GJ-05-PD-6780"
matches = re.search("[A-Z]{2}-[0-9]{2}-[A-Z]{2}-[0-9]{4}", str)
print(matches)
matches = re.search("(GJ|MH|UP)-[0-9]{2}-[A-Z]{2}-[0-9]{4}", str)
print(matches)
