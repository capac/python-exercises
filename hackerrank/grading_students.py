#! /usr/bin/env python3

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    grades = [int(g) for g in grades.split(' ')]
    new_grades = []
    for grade in grades:
        if grade < 38:
            new_grades.append(grade)
            continue
        if 5 - (grade % 5) < 3:
            new_grade = grade + 5 - (grade % 5)
            new_grades.append(new_grade)
        elif 5 - (grade % 5) >= 3:
            new_grades.append(grade)
    return new_grades


if __name__ == '__main__':
    arr = input('Provide an array of grades: ')
    result = gradingStudents(arr)
    print(result)
