t=10000
p=2020
pin=int(input("Enter pin:"))
if pin==p:
    while(True):
        print("1.Withdraw\n2.Enquire\n3.Exit\n")
        ch=int(input("Enter your choice:"))
        if ch==1:
            a=int(input("Enter amount to be withdrawed:"))
            t=t-a
            print(f"{a} withdrawed.Balance={t}")
        elif ch==2:
            print(f"Balance={t}")
        elif ch==3:
            exit()
        else:
            print("Invalid entry.")
else: print("Invalid Pin.")  