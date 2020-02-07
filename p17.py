a= int(input("enter the number of natural numbers to be generated:\n"))
print("the first",a, "natural numbers in descending order are:")
for i in range(a,0,-1):
    print(i,end=' ')
