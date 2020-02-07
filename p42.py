n= int(input("enter any number"))
sum=0
while n>0:
    a= n%10
    n=n//10
    sum =sum+a
print("the sum of digits of entered number is ",sum)
