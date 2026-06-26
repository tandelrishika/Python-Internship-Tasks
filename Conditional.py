#Q1
n=int(input("Enter age:"))

if n <=17:
    print("Not eligible to vote")
else:
    print("Eligible to vote")

#Q2
n=int(input("Enter marks:"))

if n>=90:
    print("Grade A")
elif n>=80:
    print("Grade B")
elif n>=60:
    print("Grade C")
else:
    print("Fail")

#Q3
color =input("Enter traffic light color:").lower()

if color=="red":
    print("STOP")
elif color=="yellow":
    print("WAIT")
elif color=="green":
    print("GO")
else:
    print("Invalid color.")

#Q4
balance=int(input("Enter balance amount:"))
withdraw=int(input("Enter withdraw amount:"))

if withdraw<=balance:
    balance=balance-withdraw
    print("Withdraw successful.")
    print("Remaining balance:",balance)
else:
    print("Insufficient balance.")

#Q5
n=int(input("Enter number:"))

if n>0:
    print("Number is positive.")
elif n<0:
    print("Number is negative.")
else:
    print("Number is zero.")

#Q6
n=int(input("Enter number:"))
s=int(input("Enter starting number:"))
e=int(input("Enter ending number:"))

if n>=s and n<e:
    print("Number lies in given range.")
else:
    print("Number doesn't lie in range.")

#Q7
username=input("Enter your Username:")
password=input("Enter password:")

if username=="Rishika" and password=='12345':
    print("Login successful")
else:
    print("Invalid username or password.")

#Q8
units=int(input("Enter units:"))

if units<=100:
    bill=units*5
elif units<=200:
    bill=(100*5)+((units-100)*7)
else:
    bill=(100*5)+(100*7)+((units-200)*10)
    print("Electricity Bill is:₹",bill)

#Q9
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
m=input("Enter operator(+,-,*,/):")

if m=='+':
    print("Addition:",num1+num2)

elif m== '-':
    print("Subtraction:",num1-num2)

elif m== '*':
    print("Multiplication:",num1*num2)

elif m== '/':
    if num2!=0:
        print("Division:",num1/num2)
    else:
        print("Cannot divide by zero.")
        
else:
    print("Invalid operator.")

#Q10
a=float(input("Enter first side of triangle:"))
b=float(input("Enter second side of triangle:"))
c=float(input("Enter third side of triangle:"))

if a==b==c:
    print("Triangle is Equilateral.")
elif (a==b or a==c or b==c):
    print("Triangle is Isosceles.")
else:
    print("Triangle is Scalene.")