word = input()

if len(word) >= 2:
    print(f'{word[0:2]}...{word[0:2]}...{word}?')
else:
    print('oh...')