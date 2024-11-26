# hello world 1
print("\"Hello, World!\"")

# hello world 2
print("Hello World\tHello World")

# Hello World with a new line
print("Hello World\nHello World")

#Student Details
name=input()
age=int(input())
CGPA=float(input())
grade=input()
cg=int(CGPA*100)/100.0
print(f"Name: {name}")
print(f"Age: {age}")
print(f"CGPA: {cg:.2f}")
print(f"Grade: {grade}")

#ASCII Values - I
char=input()
print(ord(char))

#ASCII Values - II
integer=int(input())
print(chr(integer))

#Round Off
import math
num=float(input())
print(int(num))
print(math.ceil(num))
print(math.floor(num))
