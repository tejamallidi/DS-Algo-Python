def linear_search(numbers_list, number_to_find):
    for index, number in enumerate(numbers_list):
        if number == number_to_find:
            return index
    return -1


def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list)-1

    while left_index <= right_index:
        mid_index = (left_index+right_index)//2  # Integer divison
        mid_number = numbers_list[mid_index]
        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index+1

        if mid_number > number_to_find:
            right_index = mid_index-1
    return -1


def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index+right_index)//2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]
    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index+1

    if mid_number > number_to_find:
        right_index = mid_index-1

    return binary_search_recursive(numbers_list, number_to_find,
                                   left_index, right_index)


def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >= 0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i < len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)


if __name__ == '__main__':
    # numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    # number_to_find = 459

    # index = linear_search(numbers_list, number_to_find)
    # print(f'Number found at {index} using linear search')

    # index = binary_search(numbers_list, number_to_find)
    # print(f'Number found at {index} using binary search')

    # index = binary_search_recursive(
    #     numbers_list, number_to_find, 0, len(numbers_list))
    # print(f'Number found at {index} using binary search')

    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 15

    indices = find_all_occurances(numbers, number_to_find)
    print(indices)
