
# Trick for bypassing Hackerrank's faulty locked code

# print_object = print
#
# def print(*items_to_print):
#     if 'Grade: ' in items_to_print:
#         items_to_print = map(str, items_to_print)
#
#         print_object(''.join(items_to_print))
#     else:
#         print_object(*items_to_print)


class Person:
    def __init__(self, _first_name, _last_name, _id_number):
        self.firstName = _first_name
        self.lastName = _last_name
        self.idNumber = _id_number

    def print_person(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):

    # Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here

    def __init__(self, _first_name, _last_name, _id_number, _scores):
        super().__init__(_first_name, _last_name, _id_number)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        grade_sum = 0
        for score in self.scores:
            grade_sum += score
        average = grade_sum / len(scores)
        if 90 <= average <= 100:
            grade = 'O'
        elif 80 <= average < 90:
            grade = 'E'
        elif 70 <= average < 80:
            grade = 'A'
        elif 55 <= average < 70:
            grade = 'P'
        elif 40 <= average < 55:
            grade = 'D'
        else:
            grade = 'T'

        return grade


if __name__ == '__main__':
    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = int(input())  # not needed for Python
    scores = list(map(int, input().split()))
    s = Student(firstName, lastName, idNum, scores)
    s.print_person()
    print("Grade: ", s.calculate())
