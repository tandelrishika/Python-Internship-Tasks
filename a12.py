#Q1
for i in range(1,11):
    print(i)

#Q2
num=int(input("Enter a number:"))
for i in range(1,11):
    print(num,"x",i ,"=" ,num*i)

#Q3
num=int(input("Enter a number:"))
factorial=1

for i in range(1,num+1):
     factorial *= i 
print("Factorial =",factorial)

#Q4
n=int(input("Enter a number:"))

a=0
b=1

for i in range(n):
    print(a, end=" ")
    a , b = b, a + b


#Q5
num = int(input("\nEnter a number:"))

if num <= 1:
    print("Number is not prime.")
else:
  for i in range(2,num):
      if num % i ==0:
        print("Number is not prime")
        break
  else:
        print("Number is prime")

#Q6
num = int(input("Enter a number:"))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num=num // 10

print("Reverse number =", reverse)

#Q7
num = int(input("Enter a number:"))
count = 0

while num > 0:
    num = num // 10
    count += 1

print("Number of digits =", count)

#Q8
# Sum of even numbers between 1-100
total = 0
for i in range(1,101):
     if i % 2 ==0:
        total += i 

print("Sum of even numbers =", total)

#Q9
n = int(input("Enter number of rows:"))

for i in range(1, n + 1):
    print(" " * (n - i) + " * " * i)

#Q10
n = int(input("Enter a number: "))

print("Divisors are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)