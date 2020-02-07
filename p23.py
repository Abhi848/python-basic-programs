n= int(input("enter the value of n:\n"))
sum=0
for i in range(1,n+1,2):
        print(i,",",end='')
        sum=sum+i
print("sum is ",sum)
