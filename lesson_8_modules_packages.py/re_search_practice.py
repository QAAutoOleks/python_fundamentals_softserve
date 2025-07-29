import re


result_1 = re.search(r"object", 
    "The method returns a match object if the search is successful")

print("Result of searching 'object' is: {}".format(result_1))
print("Only span output: {}".format(result_1.span()))