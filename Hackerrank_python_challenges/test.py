def urlify(string, length):

    """
    function replaces single spaces with %20 and removes trailing spaces
    """
    char_list = []
    for i in string:
        char_list.append(i)
    new_index = len(string)

    for i in reversed(range(length)):
        if char_list[i] == ' ':
            # Replace spaces
            char_list[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            char_list[new_index - 1] = char_list[i]
            new_index -= 1

    return char_list


if __name__ == '__main__':
    _string = "Mr Petros Ale    "
    print(urlify(_string, 13))
