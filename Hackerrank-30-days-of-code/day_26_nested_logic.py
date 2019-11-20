def fine(actual_d, due_d):
    counter = 0
    delay = [0, 0, 0]
    for pos in range(3):
        if actual_d[pos] <= due_d[pos]:
            counter += 1
        elif actual_d[pos] > due_d[pos] and actual_d[2] >= due_d[2]:
            delay[pos] = actual_d[pos] - due_d[pos]
    if counter == 3:
        return 0
    else:
        if delay[1] == 0 and delay[2] == 0:
            fee = 15 * delay[0]
        elif delay[2] == 0:
            fee = 500 * delay[1]
        else:
            fee = 10000
        return fee


if __name__ == '__main__':
    actual_date = [int(i) for i in input().split()]
    due_date = [int(i) for i in input().split()]
    # print(actual_date, due_date)
    print(fine(actual_date, due_date))
