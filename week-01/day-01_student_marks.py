
student_name = input("Enter student name: ")
mathematics = int(input("Enter Mathematics mark: "))
physics = int(input("Enter Physics mark: "))

total = mathematics + physics
average = total / 2

print("Student:", student_name)
print("Total marks:", total)
print(f"Average mark: {average:.2f}")
