"""
Student Grading System
University of Mindanao

A program that accepts student grades, calculates averages,
and provides comprehensive evaluation results.
"""



def get_remarks(average_grade):
    """
    Get remarks based on average grade.

    Args:
        average_grade (float): The calculated average grade

    Returns:
        str: Remarks for the grade
    """
    if average_grade < 0 or average_grade > 100:
        return "Invalid"
    elif average_grade < 50:
        return "Dropped"
    elif average_grade < 75:
        return "Failed"
    elif average_grade >= 75 and average_grade <= 79:
        return "Passed - Satisfactory"
    elif average_grade >= 80 and average_grade <= 84:
        return "Passed - Good"
    elif average_grade >= 85 and average_grade <= 89:
        return "Passed - Average"
    elif average_grade >= 90 and average_grade <= 99:
        return "Passed - Very Good"
    elif average_grade == 100:
        return "Passed - Excellent"


def calculate_point_grade(average_grade):
    """
    Calculate point grade from average grade.
    Formula: ((100 - Average Grade) + 10) / 10

    Args:
        average_grade (float): The calculated average grade

    Returns:
        float: Point grade
    """
    return ((100 - average_grade) + 10) / 10


def display_header():
    """Display the system header."""
    print("=" * 70)
    print(" " * 15 + "UNIVERSITY OF MINDANAO")
    print(" " * 15 + "Student Grading System")
    print("=" * 70)
    print("\nInstructions:")
    print("  • Enter grades between 0 and 100")
    print("  • Enter -1 to finish and see results")
    print("=" * 70)


def display_results(grades):
    """
    Display the final grading results.

    Args:
        grades (list): List of all entered grades
    """
    if not grades:
        print("\n⚠ No grades entered!")
        return

    # Calculate average
    average_grade = sum(grades) / len(grades)

    # Calculate point grade
    point_grade = calculate_point_grade(average_grade)

    # Get remarks
    remarks = get_remarks(average_grade)

    # Display results
    print("\n" + "=" * 70)
    print(" " * 25 + "GRADE REPORT")
    print("=" * 70)

    # Display all entered grades
    print("\nEntered Grades:")
    for i, grade in enumerate(grades, 1):
        print(f"  Grade {i}: {grade:.2f}")

    print("\n" + "-" * 70)
    print(f"Number of Grades: {len(grades)}")
    print(f"Total Sum: {sum(grades):.2f}")
    print("-" * 70)

    # Display evaluation
    print("\n" + "=" * 70)
    print(" " * 25 + "EVALUATION")
    print("=" * 70)
    print(f"Average Grade:  {average_grade:.2f}")
    print(f"Point Grade:    {point_grade:.2f}")
    print(f"Remarks:        {remarks}")
    print("=" * 70)


def validate_grade(grade):
    """
    Validate if the grade is within acceptable range.

    Args:
        grade (float): The grade to validate

    Returns:
        bool: True if valid, False otherwise
    """
    return 0 <= grade <= 100


def main():
    """Main function to run the grading system."""
    display_header()

    grades = []
    grade_count = 0

    print("\n")

    while True:
        try:
            grade_input = input(f"Enter grade #{grade_count + 1} (or -1 to finish): ").strip()
            grade = float(grade_input)

            # Check if user wants to finish
            if grade == -1:
                if grades:
                    display_results(grades)
                    break
                else:
                    print("\n⚠ No grades entered yet! Please enter at least one grade.")
                    continue

            # Validate grade
            if not validate_grade(grade):
                print(f"⚠ Invalid grade! Please enter a value between 0 and 100.")
                continue

            # Add valid grade to list
            grades.append(grade)
            grade_count += 1
            print(f"✓ Grade {grade:.2f} added successfully!")

        except ValueError:
            print("⚠ Invalid input! Please enter a numeric value.")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            break

    # Ask if user wants to process another student
    print("\n" + "=" * 70)
    another = input("Do you want to process another student? (yes/no): ").strip().lower()
    if another in ['yes', 'y']:
        print("\n")
        main()
    else:
        print("\n" + "=" * 70)
        print("Thank you for using the Student Grading System!")
        print("=" * 70)


if __name__ == "__main__":
    main()