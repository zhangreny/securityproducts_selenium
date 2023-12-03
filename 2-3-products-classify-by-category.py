with open("0-products.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
elements = []
for line in lines:
    elements.append(line.strip().split("-----"))

# 按照产品分类去排序
hashtable = {}
for ele in elements:
    if '(' in ele[4]:
        category = ele[4].split("(")[0].strip()
    elif '（' in ele[4]:
        category = ele[4].split("（")[0].strip()
    else:
        category = ele[4].strip()
    if category in hashtable:
        hashtable[category].append(ele)
    else:
        hashtable[category] = []
        hashtable[category].append(ele)

for key, value in hashtable.items():
    with open("2-3产品分类/"+key+".txt", "w", encoding="utf-8") as f:
        for v in value:
            f.write(str(v) + "\n")