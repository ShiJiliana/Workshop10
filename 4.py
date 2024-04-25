with open('input4.txt', 'r') as f:
    lines = f.readlines()
    with open('output4.txt', 'w') as f1:
        for line in lines:
            if len(line) > 21:
                print(line.strip(), file=f1)
