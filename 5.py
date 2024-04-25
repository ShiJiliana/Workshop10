result = 0
with open('input5.txt', 'r') as f:
    line_numbers = [0, 1, 2]
    lines = []
    with open('output5.txt', 'w') as f1:
        try:
            for i, line in enumerate(f):
                if i in line_numbers:
                    lines.append(int(line.strip()))
                else:
                    break
            result = lines[0] / lines[1] + lines[2]
            print(result, file=f1)
        except ValueError:
            print('data error', file=f1)
        except ZeroDivisionError:
            print('division by 0', file=f1)
