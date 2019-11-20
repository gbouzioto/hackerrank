def rotate_left(arr):
    """
    :type arr: list
    """
    first_elem = arr.pop(0)
    arr.append(first_elem)


size, left_rotations = tuple(map(int, input().split()))
array = [int(num) for num in input().split()]

i = 0
while i < left_rotations:
    rotate_left(array)
    i += 1

print(' '.join([str(num) for num in array]))
