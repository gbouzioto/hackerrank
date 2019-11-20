times = int(input())
queues = []
for i in range(times):
    n = int(input())
    queues.append(([int(num) for num in input().split()], n))

results = []
for queue in queues:
    min_bribes = 0
    for i in range(queue[1] - 1, -1, -1):
        if (queue[0][i] - 1) - i > 2:
            results.append('Too chaotic')
            min_bribes = 0
            break
        for j in range(max(queue[0][i] - 2, 0), i):
            if queue[0][j] > queue[0][i]:
                min_bribes += 1
    if min_bribes != 0:
        results.append(min_bribes)

for result in results:
    print(result)
