a= int(input("enter the 1st number num1:\n"))
b= int(input("enter the 2nd number num2:\n"))
c= int(input("enter the 3rd number num3:\n"))
if (a>=b) and (a>=c):
    largest= a
elif (b>=a) and (b>=c):
    largest= b
else:
    largest= c

print("the biggest of three numbers entered is:", largest)
