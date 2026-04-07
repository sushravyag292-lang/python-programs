name = input("Enter student name: ")
reg_no = input("Enter reg number: ")
dob = input("Enter date of birth: ")

print("Enter marks of 5 subjects:")
m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))
m4 = float(input("Subject 4: "))
m5 = float(input("Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Name:", name)
print("Reg No:", reg_no)
print("Total :", total)
print("Percentage:", percentage,)