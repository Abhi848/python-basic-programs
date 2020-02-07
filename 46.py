n= int(input("enter any number:\n"))
print("Number of prime digits in the entered number is")
c=0
for i in range(n):
    if(n%i)==0:
        c=c+1
        break
print(c)
