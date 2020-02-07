a= float(input("enter the billing amount:\n"))
if a>6000:
    b= int(a)*0.1
    c= int(a)-int(b)
    print("your net billing amount:",c)
else:
    print("your net billing amount:",a)
