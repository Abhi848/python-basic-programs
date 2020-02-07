n= int(input("enter any number"))
sum=0
temp=n
while temp>0:
    a=temp%10
    sum=sum+(a**3)
    temp=temp//10
if n==sum:
    print("it is armstrong number")
else:
    print("it is not a armstrong number")
