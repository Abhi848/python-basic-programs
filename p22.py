n= int(input("enter the value of n:\n"))
sum=0
for i in range(1,n+1):
    sum=sum+(1/i)
print("the sum of series is", round(sum,4))
