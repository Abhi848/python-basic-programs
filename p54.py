sum=0
for i in range(1,8,1):
    fact=1
    for j in range(1, (i+1), 1):
        fact= fact*j
    s= i/fact
    sum=sum+s
print(sum)
