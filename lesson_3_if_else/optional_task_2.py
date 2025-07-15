grade = int(input())

match grade:
    case a if 90 <= a <= 100:
        result = "A"
    case b if 80 <= b < 90:
        result = "B"
    case c if 70 <= c < 80:
        result = "C"
    case d if 60 <= d < 70:
        result = "D"
    case e if 50 <= e < 60:
        result = "E"
    case f if 0 <= f < 50:
        result = "F"
    case _:
        result = "Wrong number"

print(result)