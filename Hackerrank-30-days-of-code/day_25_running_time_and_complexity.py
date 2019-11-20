def is_prime(num):
    if num <= 1:
        return "Not prime"
    i = 2
    while i*i <= num:
        if num % i == 0:
            return "Not prime"
        i += 1
    return "Prime"


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        number = int(input())
        print(is_prime(number))
