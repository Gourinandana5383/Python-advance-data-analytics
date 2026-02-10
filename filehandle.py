with open("sheet1.csv","r") as f:
    lines=f.read().splitlines()
text=[line.split(",") for line in lines]
keys=text[0]
result={keys[0]:[],keys[1]:[],keys[2]:[]}
for row in text[1:]:
    result[keys[0]].append(row[0])
    result[keys[1]].append(int(row[1]))
    result[keys[2]].append(int(row[2]))
print(result)