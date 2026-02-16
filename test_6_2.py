
t = []
f = False
while f != True:
    ip = input()
    numbers = ip.split(".")
    if len(numbers) != 4:
        f = False
        print("Неправильный IP-адрес")
        continue
    for i in range(0, len(numbers)):
        if numbers[i].isdigit() == False:
            print("Неправильный IP-адрес")
            break
        t.append(int(numbers[i]))
        if 255 >= t[i] >= 0:
            f = True
        else:
            f = False
            print("Неправильный IP-адрес")
            break



numbers = [int(i) for i in numbers]
if f == True:
    if 223 >= numbers[0] >= 1:
        print("unicast")
    elif 239 >= numbers[0] >= 224:
        print("multicast")
    elif (
        numbers[0] == 255
        and numbers[1] == 255
        and numbers[2] == 255
        and numbers[3] == 255
    ):
        print("local broadcast")
    elif numbers[0] == 0 and numbers[1] == 0 and numbers[2] == 0 and numbers[3] == 0:
        print("unassigned")
    else:
        print("unused")
