n = int(input())
a = [int(i) for i in input().split()]
a.sort()
pairs = 0
previous = a.pop(0)
same = 1
for i in a:
    if i != previous:
        previous = i
        pairs += same // 2
        same = 1
    else:
        same += 1
pairs += same // 2
