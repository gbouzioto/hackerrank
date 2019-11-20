def bubble(arr):
    count_swap = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count_swap += 1
        if count_swap == 0:
            break
    print("Array is sorted in {} swaps.".format(count_swap))
    print("First Element: {}".format(arr[0]))
    print("Last Element: {}".format(arr[-1]))


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    bubble(a)
    print(a)

