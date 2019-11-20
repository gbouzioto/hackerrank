def convert_to_binary(number):
    binary = ""
    while number > 0:
        if number % 2 == 1:
            binary += "1"
        else:
            binary += "0"
        number = number // 2
    return binary[::-1]


def count_aces_in_a_row(binary):
    counter = 0
    tmp = 0
    for position, character in enumerate(binary):
        if character == '1':
            counter += 1
        elif character == '0' and binary[position - 1] == '1' and position != 0:
            if counter > tmp:
                tmp = counter
            counter = 0
    if counter > tmp:
        return counter
    else:
        return tmp


if __name__ == '__main__':

    n = int(input())
    _binary = convert_to_binary(n)
    # print(_binary)
    print(count_aces_in_a_row(_binary))

