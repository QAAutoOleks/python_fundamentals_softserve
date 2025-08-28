import pandas as pd


first_datas = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

first_frame = pd.DataFrame(first_datas)

print(first_frame)