with open("config_sw1.txt") as f:
    for line in f:
        if line.startswith('!'):
            k=1
        else:
            print(line, end='')