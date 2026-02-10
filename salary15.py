emp={"Name":["a","b","c"],"Salary":[10000,20000,30000]}
res = []
for i in emp["Salary"]:
    if i>15000:
        res.append(1)
        print("True")
    else:
        res.append(0)
        print("False")

#print("res":res)
emp["res"]=res
print(emp)