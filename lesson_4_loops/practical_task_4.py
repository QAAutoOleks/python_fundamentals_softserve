word = input()

number_of_vowels = 0
list_of_vowels = {'a', 'e', 'i', 'o', 'u'}

for i in word:
    if i in list_of_vowels:
        number_of_vowels += 1

print(number_of_vowels)