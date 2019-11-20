if __name__ == '__main__':

    N, M = map(int, input().split())
    rows = [input() for _ in range(N)]
    K = int(input())

    for _row in sorted(rows, key=lambda row: int(row.split()[K])):
        print(_row)
