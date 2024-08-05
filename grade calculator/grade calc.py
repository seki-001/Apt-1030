def get_grade(mark):
    """Return the grade based on the provided mark according to USIU's grading system."""
    if mark >= 90:
        return 'A'
    elif mark >= 85:
        return 'A-'
    elif mark >= 80:
        return 'B+'
    elif mark >= 75:
        return 'B'
    elif mark >= 70:
        return 'B-'
    elif mark >= 65:
        return 'C+'
    elif mark >= 60:
        return 'C'
    elif mark >= 55:
        return 'C-'
    elif mark >= 50:
        return 'D+'
    elif mark >= 45:
        return 'D'
    elif mark >= 40:
        return 'D-'
    else:
        return 'F'

def main():
    while True:
        user_input = input("Enter the student's mark (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Program terminated.")
            break
        try:
            mark = int(user_input)
            if 0 <= mark <= 100:
                grade = get_grade(mark)
                print(f"The grade for a mark of {mark} is: {grade}")
            else:
                print("Invalid mark. Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
