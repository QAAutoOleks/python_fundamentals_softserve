import random
names = ['Sam', 'Don', 'Sid']
code_names = ['Iron', 'Batman', 'Capitan']
secret_names = map(lambda x: random.choice(x), code_names)
print(list(secret_names))