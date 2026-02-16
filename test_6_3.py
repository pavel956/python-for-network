access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

for intf, vlan in access.items():
    print("interface FastEthernet" + intf)
    for command in access_template:
        if command.endswith("access vlan"):
            print(f" {command} {vlan}")
        else:
            print(f" {command}")
for intf in trunk.keys():
    print("interface FastEthernet" + intf)
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            iii = [(value) for  value in trunk[intf]]
            
            if iii[0] == "add":
                del iii[0]
                print(f" {command} add ", end="")
                print(*iii, sep=",")
            if iii[0] == "only":
                del iii[0]
                print(f" {command} ", end="")
                print(*iii, sep=",")
            if iii[0] == "del":
                del iii[0]
                print(f" {command} remove ", end="")
                print(*iii, sep=",")
        else:
            print(f" {command}")
