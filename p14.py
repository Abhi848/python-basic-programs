a= int(input("enter the marks scored in first subject:\n"))
b= int(input("enter the marks scored in 2nd subject:\n"))
c= int(input("enter the marks scored in 3rd subject:\n"))
t= int(a)+int(b)+int(c)
av= int(t)/3
print("total marks :", t)
print("average is:", av)
if av<35:
    print("grade: C")
elif (av>35) and (av<=60):
    print("grade: B")
else:
    print("grade: A")
