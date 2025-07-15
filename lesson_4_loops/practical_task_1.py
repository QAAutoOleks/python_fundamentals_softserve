word = input()
word = word.lower()

counter = 1
result = True

for j in word:
    for i in range(counter, len(word)):
        if j == word[i]:
            result = False
            break
    counter += 1
print(result)