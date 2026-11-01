# Check whether a number is Even or Odd
num = int(input("enter a number :"))
if num % 2 == 0:
    print("even number")
else:
    ("odd number")

# Check the Num is Positive, Negative, or Zero 
num = 10
if num > 0:
    print("positive number")
elif num < 0:
    print("negative number")
else:
    ("zero")          

#Reverse the num using for and while both a = 12345
num = 12345
digit = 0
rev = 0
for i in range(len(str(num))):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
    print("Reverse number:" ,rev)  

num = 12345
digit = 0
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit 
    num = num // 10
    print("Reverse number:",rev)  

#Check the Num is Palindrome or not
num = 1221
rev = 0
original = num
digit = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if original == rev:
    print("palindrome number")
else:
    print("not a palindrome number")        

#Check the num is prime or not
num = 11
count = 0
if num > 1:
    for i in range(1, num + 1):
     if num % i == 0:
           count += 1
    if count == 2:
        print("prime number")
    else:
        print("not a prime number")
else:
    print("not a prime number")

#Print 1 to 100 prime number
for num in range(2, 101):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
             count += 1
    if count == 2:
        print(num)      

# Find the factorial
num = 5
fact = 1
for i in range(1, num + 1):
    fact = fact * i
    print("Factorial of :",fact)

#Print square and cube of a particular number
num = 3
square = num ** 2
cube = num ** 3
print("Square :",square)
print("Cube :",cube)

# Reverse an string without using slicing
text = "cat"
rev = ""
for i in text:
    rev = [i] + rev
    print("Reverse string :",rev)

# Print Even and Odd from list
my_list = [10, 20, 25, 32, 13, 12]
print("Even number")
for i in my_list:
    if i % 2 == 0:
        print(i)
print("Odd number")
for i in my_list:
        if i % 2 != 0:
            print(i)

# Count even and odd from list
my_list=[10,15,5,35,30,12,32]
even = 0
odd = 0
for i in my_list:
  if i % 2 == 0:
    even += 1
  else:
    odd += 1
print("Even count :",even)
print("Odd count :",odd)    

# Reverse the list without using predefined function
my_list=[10,15,5,35]
rev = []
for i in my_list:
    rev = [i] + rev
    print("Reverse list :",rev)

# Print prime num from list
my_list = [2, 4, 5, 6, 8, 10, 11]
for num in my_list:
    count = 0
    if num > 1:
        for i in range (1, num + 1):
         if num % i == 0:
                count += 1
        if count == 2:
             print(num)     

# Print only string from list
my_list = [10,'ram',12,'python']
for i in my_list:
    if type(i)==str:
        print(i)

# Print only int values from list
my_list = [10,'ram',12,'python']
for i in my_list:
    if type(i)==int:
        print(i)

# Find maximum number
t = (10,20,30,40,50)
max_num = max(t)
print("Maximum number :",max_num)

# Find minimum number            
t = (10,20,30,40,50)
min_num = min(t)
print("Minimum number :",min_num)

# Find sum 
t = (10,20,30,40,50)
total = sum(t)
print("Sum :",total)

# Find the length of a tuple without using len()
t = (10,20,30,40,50)
count = 0
for i in t:
    count += 1
    print("Length :",count)

# Find the sum of tuple elements
t = (10,20,30,40,50)
total = 0
for i in t:
  total += i
  print("total :",total)

# Display only Even numbers from a tuple
t = (2, 4, 5, 6, 8, 10, 11)
for i in t:
 if i % 2 == 0:
  print(i)

# Display all keys and values of a dictionary 
my_dict = {"name":"ram","age":21,"city":"pune"}
for key,value in my_dict.items():
    print(key, ":", value)

# Find the total marks of all students
students = {"ram":80, "rahul":78, "shyam":59}
total = 0
for i in students.values():
    total += i
    print("Total marks :",total)

# Display students who scored above 60
students = {"ram":80, "rahul":78, "shyam":59}
for key,value in students.items():
    if value > 60:
        print(key , ":", value)

# Count the number of students who passed  
students = {"ram":80, "rahul":78, "shyam":89}
count = 0
for marks in students.values():
    if marks >= 35:
        count += 1
print("Passed students",count)

# Find the highest marks in a dictionary
students = {"ram":80, "rahul":78, "shyam":89}
highest = max(students.values())
print("Highest marks :",highest)


           
