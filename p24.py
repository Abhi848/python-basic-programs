n= int(input("enter n:"))
sum=0
for i in range(2,n+2):
    print(1/(i**3),"+",end=' ')
    sum=sum+(1/(i**3))
print("sum is ",sum)
