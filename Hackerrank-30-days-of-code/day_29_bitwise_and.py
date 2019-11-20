#!/bin/python3


# if __name__ == '__main__':
#     t = int(input())
#
#     for t_itr in range(t):
#         maximum = 0
#         tmp = 0
#         n, k = map(int, input().split(' '))
#
#         n_list = [i for i in range(1, n + 1)]
#         for i in n_list:
#             if i == n:
#                 break
#             for j in range(i+1, n + 1):
#                 if i & j > maximum:
#                     tmp = i & j
#                     if tmp < k:
#                         maximum = tmp
#
#         print(maximum)

T = int(input().strip())
for _ in range(T):
    n, k = map(int, input().split())
    print(k-1 if ((k-1) | k) <= n else k-2)
