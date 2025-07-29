import re


result = re.findall("[q-t]", 
        "Metacharacters are characters with a special meaning")

# \d signals a special sequence
result2 = re.findall("\d", 
        "Metacharacters are characters with 21 a special meaning")

print(result)
print(result2) # output ['2', '1']