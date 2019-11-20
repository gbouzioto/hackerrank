if __name__ == '__main__':

    loop = int(input())
    classroom = [[input(), float(input())] for _ in range(loop)]
    classroom.sort(key=lambda pair: float(pair[1]))
    # print(classroom)
    items = [[pair[0], pair[1]] for pair in classroom if pair[1] > classroom[0][1]]
    # print(items)
    second_lower_grade_students = [[pair[0], pair[1]] for pair in items if pair[1] == items[0][1]]
    # print(second_lower_grade_students)
    second_lower_grade_students.sort(key=lambda pair: str(pair[0]))
    for pair in second_lower_grade_students:
        print(pair[0])
