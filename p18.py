a=int(input("enter the lower bound value:\n"))
b=int(input("enter the upper bound value:\n"))
print("the prime numbers between ", a, "and", b, "are")
for i in range(a,b+1):
    for j in range(2,i):
        if(i%j)==0:
            break
    else:
        print(i, end=' ')
