n = int(input())
array = [int(i) for i in input().split()]

jumps = 0
i = 0
while i < n - 1:
    if array[i + 1] == 1:
        i += 2
        jumps += 1
    elif array[i + 1] == 0:
        if i + 2 <= n - 1:
            if array[i + 2] == 1:
                i += 1
                jumps += 1
            else:
                jumps += 1
                i += 2
        else:
            i += 1
            jumps += 1
print(jumps)
