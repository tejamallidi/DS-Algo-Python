def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i-1
        while j >= 0 and anchor < elements[j]:
            # swapping the largest number to smallest
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor  # assigning anchor to [j+1] position
        print(elements)


if __name__ == '__main__':
    # elements = [11, 9, 29, 7, 2, 15, 28]
    elements = [2, 1, 5, 7, 2, 0, 5]
    insertion_sort(elements)
    # print(elements)
    # tests = [
    #     [11, 9, 29, 7, 2, 15, 28],
    #     [3, 7, 9, 11],
    #     [25, 22, 21, 10],
    #     [29, 15, 28],
    #     [],
    #     [6]
    # ]
    # for elements in tests:
    #     insertion_sort(elements)
    #     print(elements)
