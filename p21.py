a= int(input("enter any number:\n"))
fact=1
if a==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,a+1):
        fact=fact*i;
print("the factorial of ",a, "is:",fact)