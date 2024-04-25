new = ''
with open('input3.txt', 'r') as f:
    with open('output3.txt', 'w') as f1:
        lines = f.readlines()
        for line in lines:
            new += line[0]
        print(new, file=f1)