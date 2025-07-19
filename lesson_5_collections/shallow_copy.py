original = [[1, 2], [3, 4]]
shallow = original.copy()
original.append(99) # змінюється тільки один список
print(original)
print(shallow)

original[0].append(777) # змінюються обидва списки
print(original)
print(shallow)

# елементи в списках - це ті ж самі обʼєкти
# або ж посилання на ті ж самі обʼєкти
# (в тому числі вкладені списки)
# але самі списки original/shallow - це різні обʼєкти