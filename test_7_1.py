with open("ospf.txt") as f:
    for line in f:
        prefix = line.split()[1]
        AD = line.split()[2].strip("]" "[")
        next = line.split()[4].strip(",")
        update = line.split()[5].strip(",")
        out = line.split()[-1]
        print("{:<20}{:<20}".format("Prefix", prefix))
        print("{:<20}{:<20}".format("AD/Metric", AD))
        print("{:<20}{:<20}".format("Next-Hop", next))
        print("{:<20}{:<20}".format("Last update", update))
        print("{:<20}{:<20}".format("Outbound Interface", out))
        print("")
