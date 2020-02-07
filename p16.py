
a = int(input("enter any number\n"))
for i in range(2,a):
    if (a%i)==0:
        print("entered number", a, "is not a prime number")
        break
    else:
        print("entered number", a, "is a prime number")
