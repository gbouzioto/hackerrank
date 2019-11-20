
if __name__ == '__main__':
    n = int(input())
    phone_book = {}
    for i in range(0, n):
        key, value = input().rstrip().split()
        phone_book[key] = value
    # print(phone_book)
    while 1:
        try:
            line = input()
            if line in phone_book:
                print("{0}={1}".format(line, phone_book[line]))
            else:
                print("Not found")
        except EOFError:
            break
