with open('somefile.txt', 'w', encoding='utf-8') as f:
    f.write('Hello SoftServe!')
    f.close()

with open('somefile.txt', 'r', encoding='utf-8') as r:
    read_result = r.read()
    print(read_result)
    r.close()