from itertools import product

if __name__ == '__main__':
    K, M = map(int, input().split())
    max_list = []
    L = ([i for i in map(int, input().split())][1::] for _ in range(K))
    results = map(lambda s: sum(pow(i, 2) for i in s) % M, product(*L))
    print(max(results))
