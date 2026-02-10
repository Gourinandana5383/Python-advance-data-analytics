with open("sheet1.csv","r") as f:
    lines=f.read().splitlines()
print(lines)
text=[line.split(",") for line in lines]
print(text)
keys=text[0]
emp={key:[] for key in keys}
for row in text[1:]:
    for i in range(len(keys)):
        val=row[i]
        if val.isdigit():
            val=int(val)
        emp[keys[i]].append(val)
print(emp)
