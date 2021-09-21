anchors = ["id",
           "nom",
           "desserte",
           "pmr",
           "ascenseur",
           "escalator",
           "gid",
           "last_update",
           "last_update_fme"]

anchors_tab = ["coordinates"]


def get_val(line):
    for anchor in anchors:
        if "\"" + anchor + "\"" in line:
            beg = anchor + "|"
            if ": \"" in line:
                return beg + "\"" + line.split(": \"")[1].split("\"")[0] + "\""
            else:
                return beg + line.split(": ")[1].split(",")[0]


f_in = open("datasetCoord.json")
f_out = open("datasetCoord.csv", "w")

for line in f_in:
    res = get_val(line)
    if res != None:
        print(res)
        f_out.write(res.split("|")[1] + ",")

    elif anchors_tab[0] in line:
        res = [0.00, 0.00]
        res[0] = f_in.readline().split("                ")[1].split(",")[0]
        res[1] = f_in.readline().split("                ")[1]
        print(anchors_tab[0] + "X|" + res[0])
        print(anchors_tab[0] + "Y|" + res[1])

        f_out.write(res[0] + "," + res[1])

f_out.close()
f_in.close()
