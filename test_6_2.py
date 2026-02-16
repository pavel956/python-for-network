ip = input()
numbers = ip.split(".")
numbers = [int(i) for i in numbers]

if 223 >= numbers[0] >= 1:
    print("unicast")
elif 239 >= numbers[0] >= 224:
    print("multicast")
elif (
    numbers[0] == 255 and numbers[1] == 255 and numbers[2] == 255 and numbers[3] == 255
):
    print("local broadcast")
elif numbers[0] == 0 and numbers[1] == 0 and numbers[2] == 0 and numbers[3] == 0:
    print("unassigned")
else:
    print("unused")
