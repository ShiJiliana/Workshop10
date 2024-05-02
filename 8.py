with open('input8.txt', 'r') as f:
    lines = f.readlines()
    all_numbers = []
    for line in lines:
        all_numbers.append(int(line.strip()))

    with open('output8.txt', 'w') as f1:
        if len(all_numbers) == 365:
            print('Обычный год', file=f1)
            print(sum(all_numbers[:31]) // 31, file=f1)
            print(sum(all_numbers[31:59]) // 28, file=f1)
            print(sum(all_numbers[59:90]) // 31, file=f1)
            print(sum(all_numbers[90:120]) // 30, file=f1)
            print(sum(all_numbers[120:151]) // 31, file=f1)
            print(sum(all_numbers[151:181]) // 30, file=f1)
            print(sum(all_numbers[181:212]) // 31, file=f1)
            print(sum(all_numbers[212:243]) // 31, file=f1)
            print(sum(all_numbers[243:273]) // 30, file=f1)
            print(sum(all_numbers[273:304]) // 31, file=f1)
            print(sum(all_numbers[304:334]) // 30, file=f1)
            print(sum(all_numbers[334:]) // 31, file=f1)

        elif len(all_numbers) == 366:
            print('Високосный год', file=f1)
            print(sum(all_numbers[:31]) // 31, file=f1)
            print(sum(all_numbers[31:60]) // 29, file=f1)
            print(sum(all_numbers[60:91]) // 31, file=f1)
            print(sum(all_numbers[91:121]) // 30, file=f1)
            print(sum(all_numbers[121:152]) // 31, file=f1)
            print(sum(all_numbers[152:182]) // 30, file=f1)
            print(sum(all_numbers[182:213]) // 31, file=f1)
            print(sum(all_numbers[213:244]) // 31, file=f1)
            print(sum(all_numbers[244:274]) // 30, file=f1)
            print(sum(all_numbers[274:305]) // 31, file=f1)
            print(sum(all_numbers[305:335]) // 30, file=f1)
            print(sum(all_numbers[335:]) // 31, file=f1)

        else:
            print('Недостаточно данных', file=f1)