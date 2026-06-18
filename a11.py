#Q1
name = input("Enter name:")
age = int(input("Enter age:"))
city = input("Enter your city:")
print("My name is", name, ",I am" ,age, "years old and I live in" ,city, ".")

#Q2
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
result = a + b
print("Result=",result)

#Q3
celsius=float(input("Enter tenperature in Celsius:"))

farenheit=(celsius * 9/5) + 32

print("Temperature in Farenheit:", farenheit)

#Q4
name = "Rishika"
print(name.upper())

#Q5
current_year=int(input("Enter current year:"))
birth_year=int(input("Enter your birth year:"))
age=current_year - birth_year
print("Your age is:",age)

#Q6
a=input("Enter first value:")
b=input("Enter second value:")

print("Before swapping:")
print("a=",a)
print("b=",b)

a,b = b,a 

print("After swapping:")
print("a=",a)
print("b=",b)

#Q7
a=int(input("Enter length of rectangle:"))
b=int(input("Enter breadth of rectangle:"))

area= a * b
print("Area of rectangle:",area)

#Q8
a=int(input("Enter a value:"))
if a >=0:
    print("Number is positive.")
else:
    print("Number is negative.")

#Q9
a=int(input("Enter first number:"))
b=int(input("Enter secong number:"))

average = (a + b)/2
print("Average of two numbers is:",average)