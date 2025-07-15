card = str(input())

if len(card) < 16:
    card = "Invalid card"
else:
    card = f"************{card[12:]}"

print(card)