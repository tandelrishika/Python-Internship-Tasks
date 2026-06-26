#Q1
a=int(input("Enter numerator:"))
b=int(input("Enter denominator:"))

if a>b:
    c=a/b
    print("Remainder is:",c)
else:
    print("Not divisible.")

#Q2
n=int(input("Enter a number:"))

if n%2==0:
    print("Number is even.")
else:
    print("Number is odd.")

#Q3
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

if a>b:
    print("Larger number is:",a)
elif b>a:
    print("Larger number is:",b)
else:
    print("Number is equal.")

#Q4
n=int(input("Enter number:"))

square= n * n 
print("Square of number is:",square)
cube= n * n * n
print("Cube of number is:",cube)

#Q5
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

if a==b:
    print("Entered Numbers are equal.")
else:
    print("Entered numbers are not equal.")

#Q6
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

if a>=0 and b>=0:
    print("TRUE.")
else:
    print("FALSE.")

#Q7
n=float(input("Enter number:"))

n=int(n)
print("Integer is:",n)

#Q8
n=(input("Enter number in string:"))

n=int(n)
n= n * 10
print("Integer is:",n)

#Q9
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

if a>=0 and b>=0:
    print("Number is positive")
else:
    print("Numbers are not positive.")

if a==0 or b==0:
    print("Atleast one number is zero.")
else:
    print("Both number are not zero.")

#Q10
a=int(input("Enter numerator number:"))
b=int(input("Enter denominator number:"))

quotient= a//b
remainder=a%b
print("Quotient is:",quotient)
print("Remainder is:",remainder)