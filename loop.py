# Print "Hello" 10 times
for i in range(1,11):
    print("Hello")

# Print numbers from 1 to 100
for i in range(1,101):
    print(i)

# Print numbers from 1 to 50 with a step of 2
for i in range(1,51,2):
    print(i)

# Print numbers from 10 to 1
for i in range(10,0,-1):
    print(i)

# Print numbers from 50 to 1.
for i in range(50,0,-1):
    print(i)

# Print numbers from -10 to 10.
for i in range(-10,11):
    print(i)

# Print numbers from 10 to -20.
for i in range(10,-21,-1):
    print(i)

# Print numbers from -10 to -50.
for i in range(-10,-51,-1):
    print(i)

# Print multiple of 5 from 5 to 100.
for i in range(5,101,5):
    print(i) 

# Print all odd numbers from 1 to 100.
for i in range(1,101):
    if i % 2 != 0:
        print(i)

# Print all even numbers from 1 to 100.
for i in range(1,101):
    if i % 2 == 0:
        print(i)

# Print numbers divisible by 3 from 1 to 50.
for i in range(1,51):
    if i % 3 == 0:
        print(i)

# Print numbers divisible by both 3 and 5 from 1 to 100.
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# Print squares of numbers from 1 to 10.
for i in range(1,11):
    print(i**2)

# Print cubes of numbers from 1 to 10.
for i in range(1,11):
    print(i**3)

# Print the multiplication table of 6.
for i in range(1,11):
    print("6 x",i,"=",6 * i)

# Print multiplication table from 1 to 5.
for i in range(1,6):
    for j in range(1,11):
        print(i, "X", j, "=", i * j)
    print()    

# Find the sum of numbers from 1 to 10.
sum = 0
for i in range(1,11):
    sum += i
print(sum )    

# Find the sum of even numbers from 1 to 100.
count = 0
for i in range(2,101,2):
    count += i
print(count)    

# Print the ASCII value of a.
print(ord("a"))

# Print ASCII values of A to Z.
for i in range(65,91):
    print(chr(i),ord(chr(i)))

# Print ASCII values of a to z.
for i in range(97,123):
    print(chr(i),ord(chr(i)))

# print A to Z
for i in range(65,91):
    print(chr(i))

# Print ASCII values of digits 0 to A.
for i in range(48,66):
    print(chr(i),i)

# Print the characters from Z to A.
for i in range(90,64,-1):
    print(chr(i))

# Print each character of "Harshada" on a new line.
text= "Harshada"
for i in text:
    print(i)

# Find the factorial of 5.
fact = 1
for i in range(1,6):
    fact = fact * i
print(fact)    

# Find the factorial of 7.
fact = 1
for i in range(1,8):
    fact = fact * i
print(fact) 

# Print the digit of 12345 in reverse order.
num = 12345
for i in (str(num)[::-1]):
    print(i)   

# Find the sum of digit of 12345.
num =  12345
sum = 0
for i in (str(num)):
    sum += int(i)
print(sum) 

# Count the digits in 1234567.
num = 1234567
count = 0
for i in (str(num)):
    count += 1
print(count)    

# Find the sum of squares from 1 to 10.
sum = 0
for i in range(1,11):
    sum += i ** 2
print(sum)    

# Print the first 10 multiples of 7.
for i in range(1,11):
    print(7 * i)

# Count the number os vowels in "Programming"
text = "Programming"
count = 0
for ch in text:
    if ch in "aeiou":
        count += 1
print(count) 

# Count the number of characters in "Python Programming" including space.
text = "Python Programming"
count = 0
for ch in text:
    count += 1
print(count)  

# Print numbers from 1 to 10 with their power 4.
for i in range(1,11):
    print(i**4) 

# # Print the numbers from 1 to 20 that are divisible by 4.
for i in range(1,21):
    if(i % 4 == 0):
     print(i)

# # Print the sum of odd numbers from 1 to 20.
sum = 0
for i in range(1,21,2):
    sum += i
print(sum) 

# # Print this pattern
# *
# **
# ***
# ****
# *****
for i in range(1,6):
    print(i * "*")   

# # Reverse the string
text = "Python"
for i in text[::-1]:
    print(i)

print(text[::-1])   

# # Check whether 7 is a prime number.
num = 7
count = 0
for i in range(1,8):
    if num % i == 0:
        count += 1
if count == 2:
        print("Prime number")
else:
     print("Not a Prime number")       

# # Print all prime numbers from 1 to 50.
for num in range(2,51):
    count = 0
    for i in range(1,num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(num)       


