
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

# Function to validate student marks
def validate_marks(mark1, mark2):
    return 0 <= mark1 <= 100 and 0 <= mark2 <= 100

# New feature: Determine pass or fail
def calculate_status(average):
    if average >= 60:
        return "Pass"
    else:
        return "Fail"

# Student marks
mark1 = 80
mark2 = 90

# Validate marks before calculating results
if validate_marks(mark1, mark2):
    average = calculate_average(mark1, mark2)
    grade = calculate_grade(average)
    status = calculate_status(average)

    # Display the results
    print("Average:", average)
    print("Grade:", grade)
    print("Status:", status)
else:
    print("Error: Marks must be between 0 and 100.")

