arr = []
for i in range(6):
    arr.append([int(n) for n in input().split()])
hourglass_sum = 0
for i in range(len(arr) - 2):
    for j in range(1, len(arr[i]) - 1):
        tmp_hourglass_sum = arr[i][j] + arr[i][j + 1] + arr[i][j - 1] + \
                            arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j + 1] + \
                            arr[i + 2][j - 1]
        if (0, 1) == (i, j) and tmp_hourglass_sum < 0:
            hourglass_sum = tmp_hourglass_sum
        hourglass_sum = max(tmp_hourglass_sum, hourglass_sum)
print(hourglass_sum)
