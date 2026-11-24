
# Student Grade Calculator

# Function to calculate the average
def calculate_average(mark1, mark2):
    return (mark1 + mark2) / 2

# Function to determine letter grade
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# Student marks
mark1 = 80
mark2 = 90

# Calculate average and grade
average = calculate_average(mark1, mark2)
grade = calculate_grade(average)

# Display the results
print("Average:", average)
print("Grade:", grade)

