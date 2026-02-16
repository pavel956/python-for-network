mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
newmac =[]
for i in range(len(mac)):
    newmac.append((".").join(mac[i].split(":")))
    
print(newmac)
