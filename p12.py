a= int(input("enter the bill amount:\n"))
b= input("do you have a membership card?\n")
if b=="y":
    c= (int(a)*0.1)
    d= int(a)-c
    print("thank you! your total bill amount is rs", a, "discount is rs", c, "and net payable is rs ",d)
else:
    e= int(a)*0.03
    f= int(a)-e
    print("thank you! your total bill amount is rs", a, "discount is rs", e, "and net payable is rs ",f)
