import datetime as d

with open('input10.txt', 'r') as f:
    lines = f.read().splitlines()
    numbers = []
    date_now = d.datetime.strptime(lines[0], '%d.%m')
    for line in lines[2:]:
        num, date = line.split()
        date = d.datetime.strptime(date, '%d.%m')
        if (date_now - date).days > 3:
            numbers.append(num)
    with open('output10.txt', 'w') as f1:
        f1.write('\n'.join(numbers))