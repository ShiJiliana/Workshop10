import os

if not os.path.isdir('simple'):
    os.mkdir('simple')

with open('input9.txt', 'r') as f:
    lines = f.readlines()
    h = []
    h1 = []
    for line in lines:
        h.append(line.strip())
    h1 = h[1::2]
    with open('output9.txt', 'w') as f1:
       f1.write('\n'.join(h1))

os.replace('output9.txt', 'simple/output9.txt')