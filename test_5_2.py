ip = input()  # ввод числа
mask = int((ip.split("/"))[-1])  # вытасекиваем маску
ip2 = (ip.split("/")[0]).split(".")
ip3 = ", ".join(ip2)  # собираем IP
iip0 = int(ip2[0])  # делим по октетам
iip1 = int(ip2[1])
iip2 = int(ip2[2])
iip3 = int(ip2[3])
binmask = "1" * int(mask) + "0" * (32 - int(mask))  # маска в двоичном виде
binmask0 = int(binmask[0:8], 2)  # делим маску на 4 октета
binmask1 = int(binmask[8:16], 2)
binmask2 = int(binmask[16:24], 2)
binmask3 = int(binmask[24:32], 2)
# вывод
ip_template = """  

IP address:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}

mask:
/{8:<8}
{4:<8} {5:<8} {6:<8} {7:<8}
{4:08b} {5:08b} {6:08b} {7:08b}
"""

print(
    ip_template.format(
        iip0, iip1, iip2, iip3, binmask0, binmask1, binmask2, binmask3, mask
    )
)
