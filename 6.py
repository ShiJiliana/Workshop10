with open('input6.txt', 'r') as f:
    with open('output6.txt', 'w') as f1:
        try:
            number_str = int(f.readline())
            num_real = len(f.readlines())
            if number_str == num_real:
                print('YES', file=f1)
            else:
                print('NO', file=f1)
        except ValueError:
            print('ERROR', file=f1)
