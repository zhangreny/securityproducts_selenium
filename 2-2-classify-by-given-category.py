with open("0-products.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

allcategories = {}
for line in lines:
    categorystr = line.strip().split("-----")[4]
    if "(" in categorystr:
        category = categorystr.split("(")[0]
        adj = categorystr.split("(")[1].split(")")[0]
    elif "（" in categorystr:
        category = categorystr.split("（")[0]
        adj = categorystr.split("（")[1].split("）")[0]
    else:
        category = categorystr
        adj = ""
    if category not in allcategories:
        allcategories[category] = []
        if adj != "":
            allcategories[category].append(adj)
    else:
        if adj not in allcategories[category] and adj != "":
            allcategories[category].append(adj)

with open("1-given-categories.txt", "w", encoding="utf-8") as f:
    for key, value in allcategories.items():
        if len(value) >= 1:
            f.write(key + "\n")
            for v in value:
                f.write("    " + v + "\n")
        else:
            f.write(key + "\n")
            