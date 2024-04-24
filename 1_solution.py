with open('input.txt', 'r') as f:
    text = f.read()
    with open('output.txt', 'a') as f1:
        text_new = text.upper()
        print(text_new, file=f1)