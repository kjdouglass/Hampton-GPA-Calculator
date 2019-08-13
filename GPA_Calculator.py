import grading_scale


def calculate_gpa():
    # Validate user input to ensure integer
    while True:
        try:
            total_courses = int(raw_input('How many classes are you taking?: '))
        except ValueError:
            print('Number must be an integer! Try again.')
            continue
        else:
            break

    # Dictionary to keep track of course data (Course#, grade, credit hours)
    course_data_dict = {}

    # Allow user to input grade received and how many credits the course was worth
    for course_num in range(1, total_courses + 1):

        # Ideally the code validates if the grade the user entered is in the
        # grading_values dictionary from the grading_scale file. Then it
        # checks if the credit hours is an integer and between 1-4.

        course_data_dict[course_num] = raw_input('Enter the grade you earned in course {}: '
                                                 .format(course_num)).upper(),\
                                       int(input('Enter the number credit hours for the course {}: '
                                                 .format(course_num)))

    # Initialize variables that go into GPA calculation
    quality_points = 0
    credit_hours = 0

    # Keep track of quality points and credit hours
    for x in course_data_dict:
        quality_points += grading_scale.grading_values[str(course_data_dict[x][0])] * float(course_data_dict[x][1])
        credit_hours += float(course_data_dict[x][1])

    # Formula to calculate GPA
    gpa = quality_points/credit_hours

    # Print quality points, credit hours and semester GPA
    print('\n')
    print('Total quality points is: {}'.format(quality_points))
    print('Total credit hours taken is: {}'.format(credit_hours))
    print('Your GPA this semester is a {} '.format(round(gpa, 2)))


def main():
    calculate_gpa()


if __name__ == '__main__':
    main()
