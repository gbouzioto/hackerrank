
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    # print(arr)
    arr.reverse()
    print(' '.join([str(i) for i in arr]))

