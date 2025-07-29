import re

result_1 = re.match(r"object", 
    "The method returns a match object if the search is successful")

result_2 = re.match(r"The", 
    "The method returns a match object if the search is successful")

print("Result of matching 'object' is: {}".format(result_1)) # None
print("Result of matching 'The' is: {}".format(result_2))

# re.match() only matches at the beginning of the string