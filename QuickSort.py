def swap(start, end, elements):
    if start != end:  # not when start and end are at same index
        temp = elements[start]
        elements[start] = elements[end]
        elements[end] = temp


def partition(elements, start, end):
    # select pivot index, get pivot
    pivot_index = start
    pivot = elements[pivot_index]

    # # start, end pointers
    # start = pivot_index + 1
    # end = len(elements) - 1

    # till start crosses end
    while start < end:
        # start and move to position untill elements[start] <= pivot
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        # end will move to position where elements[end] > pivot
        while elements[end] > pivot:
            end -= 1
        # when we stop, if start < end, swap the two numbers at start and end indices
        if start < end:
            swap(start, end, elements)
    # swap end with pivot
    swap(pivot_index, end, elements)

    # return the final position of pivot - end
    return end


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        # call the quick_sort function recursively on left , right parts of the "pi"
        quick_sort(elements, start, pi-1)  # left partition
        quick_sort(elements, pi+1, end)  # right partition


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    for elements in tests:
        quick_sort(elements, 0, len(elements) - 1)
        print(elements)
