word = str(input())
word = word.lower()

if word.count('x') == word.count('o'):
    print(True)
elif word.count('x') != word.count('o'):
    print(False)
else:
    print(True)