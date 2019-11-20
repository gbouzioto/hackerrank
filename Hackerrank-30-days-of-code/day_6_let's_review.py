

def break_string(_string):
    n = len(_string)
    subs1 = ""
    subs2 = ""
    for _i in range(0, n):
        if _i % 2 == 0:
            subs1 += (_string[_i])
        else:
            subs2 += (_string[_i])
    print("{0} {1}".format(subs1, subs2))


if __name__ == '__main__':
    N = int(input())
    for i in range(0, N):
        break_string(str(input()))
