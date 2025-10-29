# Student Marks Calculator

# Take input for 5 subjects
subjects = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    subjects.append(mark)

# Calculations
total = sum(subjects)
average = total / 5

# Grade logic
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

# Display output
print("\n---- Result ----")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Grade: {grade}")

# Save to a file
with open("result.txt", "w") as file:
    file.write("----- Student Result -----\n")
    file.write(f"Marks: {subjects}\n")
    file.write(f"Total: {total}\n")
    file.write(f"Average: {average}\n")
    file.write(f"Grade: {grade}\n")

print("\nResult saved to result.txt ✅")
