# Grade Checker Program

print("=== Grade Checker ===")

name = input("Enter your name: ")
marks = float(input("Enter your marks (0 - 100): "))

# Validate input
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter a value between 0 and 100.")
else:
    # Determine grade
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    # Display result
    print("\n----- Result -----")
    print("Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)

    if grade == "F":
        print("Status: Failed")
    else:
        print("Status: Passed")
