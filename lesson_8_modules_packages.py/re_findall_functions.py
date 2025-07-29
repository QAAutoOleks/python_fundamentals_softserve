import re


# '*' Zero or more occurences
# '+' One or more occurences 
# '{}' Exactly the specified number of occurences
# '|' Either or

pattern = "Hello SoftServe IT Academy SoftServe every day"

# Check if the string contains "er" followed by 0 or more "x" characters:
result_1 = re.findall("erx*", pattern)
# Check if the string contains "ai" followed by 1 or more "x" characters:
result_2 = re.findall("dwx+", pattern)
# Check if the string contains "e" followed by exactly two "l" characters:
result_3 = re.findall("el{2}", pattern)
# Check if string contains either "IT" or "day":
result_4 = re.findall("IT|day", pattern)

print(result_1)
print(result_2)
print(result_3)
print(result_4)