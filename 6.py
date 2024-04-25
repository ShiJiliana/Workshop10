line_numbers = []
num_real = 0
with open('input6.txt', 'r') as f:
    with open('output6.txt', 'w') as f1:
        try:
            number_str = int(f.readline())
            for i in range(1000):
                line_numbers.append(i)
            for i, line in enumerate(f):
                if i in line_numbers:
                    num_real += 1
                else:
                    break
            if number_str == num_real:
                print('YES', file=f1)
            else:
                print('NO', file=f1)
        except ValueError:
            print('ERROR', file=f1)
