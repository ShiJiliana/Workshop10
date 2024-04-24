with open('input2.txt', 'r') as f:
    with open('output2.txt', 'a') as f1:
        lines = f.readlines()
        for line in lines:
            if line[0] == 'a' or line[0] == 'A':
                print(line.strip(), file=f1)

