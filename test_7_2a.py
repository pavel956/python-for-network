with open("config_sw1.txt") as f:
    for line in f:
        iii = True
        if line.startswith("!"):
            k = 1
        else:
            ignore = ["duplex", "alias", "configuration"]
            for j in ignore:
                if j in line:
                    iii = False
                    break
            if iii == True:
                print(line, end="")
