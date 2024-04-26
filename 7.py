with open('input7.txt', 'r+') as f:
    lines = f.readlines()
    f.seek(0)
    f.truncate()
    for line in lines:
        k = int(line.strip())
        if k != 100:
            f.write(str(k) + '\n')
