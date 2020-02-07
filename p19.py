a= int(input("enter the upper bound number to generate the fibonacci numbers"))
n1=0
n2=1
print("fibonacci numbers up to the entered number is :")
print(n1,n2,end=' ')
for i in range(2,a-1):
    n3=n1+n2
    print(n3,end=' ')

    n1=n2
    n2=n3
