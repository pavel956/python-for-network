interface = {
    "access": {
        "switchport mode access",
        "switchport access vlan {}",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
    },
    "trunk": {
        "switchport trunk encapsulation dot1q",
        "switchport mode trunk",
        "switchport trunk allowed vlan {}",
    },
}


regime = input("Введите режим работы интерфейса (access/trunk): ")
number_tip = input("Введите тип и номер интерфейса: ")
vlans = input("Введите номер влан(ов):  ")
print()
print("interface {}".format(number_tip))
print("\n".join(interface[regime]).format(vlans))
