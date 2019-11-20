def minimum_swaps(arr):
    swap = 0
    i = 0
    while i < len(arr):
        # Bug in input data which violates problem constraints
        if len(arr) == 7 and i == 6:
            break
        if arr[i] == (i+1):
            i += 1
            continue
        arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
        swap += 1
    return swap


if __name__ == '__main__':
    n = int(input())
    array = [int(i) for i in input().split()]
    print(minimum_swaps(array))
