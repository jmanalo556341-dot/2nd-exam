class StudentGradingSystem:
    def __init__(self):
        self.grades = []
        self.grade_count = 0

    def get_remarks(self, average_grade):
        if average_grade < 0 or average_grade > 100:
            return "Invalid"
        elif average_grade < 50:
            return "Dropped"
        elif average_grade < 75:
            return "Failed"
        elif average_grade <= 79:
            return "Passed - Satisfactory"
        elif average_grade <= 84:
            return "Passed - Good"
        elif average_grade <= 89:
            return "Passed - Average"
        elif average_grade <= 99:
            return "Passed - Very Good"
        elif average_grade == 100:
            return "Passed - Excellent"

    def calculate_point_grade(self, average_grade):
        return ((100 - average_grade) + 10) / 10

    def display_header(self):
        print("=" * 70)
        print(" " * 15 + "UNIVERSITY OF MINDANAO")
        print(" " * 15 + "Student Grading System")
        print("=" * 70)
        print("\nInstructions:")
        print("  • Enter grades between 0 and 100")
        print("  • Enter -1 to finish and see results")
        print("=" * 70)

    def display_results(self):
        if not self.grades:
            print("\n⚠ No grades entered!")
            return
        average_grade = sum(self.grades) / len(self.grades)
        point_grade = self.calculate_point_grade(average_grade)
        remarks = self.get_remarks(average_grade)
        print("\n" + "=" * 70)
        print(" " * 25 + "GRADE REPORT")
        print("=" * 70)
        for i, grade in enumerate(self.grades, 1):
            print(f"  Grade {i}: {grade:.2f}")
        print("\n" + "-" * 70)
        print(f"Number of Grades: {len(self.grades)}")
        print(f"Total Sum: {sum(self.grades):.2f}")
        print("-" * 70)
        print("\n" + "=" * 70)
        print(" " * 25 + "EVALUATION")
        print("=" * 70)
        print(f"Average Grade:  {average_grade:.2f}")
        print(f"Point Grade:    {point_grade:.2f}")
        print(f"Remarks:        {remarks}")
        print("=" * 70)

    def validate_grade(self, grade):
        return 0 <= grade <= 100

    def process_grades(self):
        self.display_header()
        while True:
            try:
                grade_input = input(f"Enter grade #{self.grade_count + 1} (or -1 to finish): ").strip()
                grade = float(grade_input)
                if grade == -1:
                    if self.grades:
                        self.display_results()
                        break
                    else:
                        print("\n⚠ No grades entered yet! Please enter at least one grade.")
                        continue
                if not self.validate_grade(grade):
                    print(f"⚠ Invalid grade! Please enter a value between 0 and 100.")
                    continue
                self.grades.append(grade)
                self.grade_count += 1
                print(f"✓ Grade {grade:.2f} added successfully!")
            except ValueError:
                print("⚠ Invalid input! Please enter a numeric value.")
            except KeyboardInterrupt:
                print("\n\nProgram interrupted by user.")
                break

    def ask_for_another_student(self):
        print("\n" + "=" * 70)
        another = input("Do you want to process another student? (yes/no): ").strip().lower()
        if another in ['yes', 'y']:
            print("\n")
            self.reset_system()
            self.process_grades()
        else:
            print("\n" + "=" * 70)
            print("Thank you for using the Student Grading System!")
            print("=" * 70)

    def reset_system(self):
        self.grades = []
        self.grade_count = 0


if __name__ == "__main__":
    system = StudentGradingSystem()
    system.process_grades()
    system.ask_for_another_student()
