name=str(input("Enter your name:"))
age=int(input("Enter your age:"))
CGPA=float(input("Enter your CPGA:"))
grade=input("Enter your Grade:")
print("Name:",name)
print("Age:",age)
cgpa_formatted=float(format(CGPA,".3f"))
cgpa=(cgpa_formatted*1000)
modified_cgpa=str(cgpa)
first_three=modified_cgpa[:3]
integer=int(first_three)
print("CGPA:",(integer/100))
print("Grade:",grade)


name=str(input())
age=int(input())
CGPA=float(input())
grade=input()
cg=int((cgpa*100)/100.0)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"CGPA: {CGPA:.2f}")
print(f"Grade: {grade}")
