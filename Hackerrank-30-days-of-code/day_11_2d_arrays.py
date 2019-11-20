if __name__ == '__main__':
    arr = []
    hourglass_sum = 0
    tmp = 0
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(4):
        for j in range(4):
            sub_sum_1 = 0
            sub_sum_2 = 0
            hourglass_1 = arr[i][j], arr[i][j + 1], arr[i][j + 2]
            hourglass_2 = arr[i + 1][j + 1]
            hourglass_3 = arr[i + 2][j], arr[i + 2][j + 1], arr[i + 2][j + 2]
            for item in hourglass_1:
                sub_sum_1 += item
            for item_1 in hourglass_3:
                sub_sum_2 += item_1
            hourglass_sum = sub_sum_1 + hourglass_2 + sub_sum_2
            if j == 0 and i == 0:
                tmp = hourglass_sum
            if hourglass_sum > tmp:
                tmp = hourglass_sum
    if hourglass_sum > tmp:
        print(hourglass_sum)
    else:
        print(tmp)
