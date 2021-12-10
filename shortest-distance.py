#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
# If the book is n pages long, and a student wants to turn to page p, what is the minimum number of pages to turn?
# They can start at the beginning or the end of the book.
# Given n and p find and print the minimum number of pages that must be turned in order to arrive at page .

def pageCount(n, p):
    # Write your code here
    if p >= n or p == n-1 or p == 1:
        return 0
    pages = []
    pages_dict = {}
    for i in range(1, n+1):
        if i == 1:
            pages_dict[i] = i
        elif i == n:
            break
        else:
            if i > 2 and pages[-1][1] < n-1:
                pages_dict[i] = (pages[-1][1]+1, pages[-1][1]+2)
            elif i <= 2 and i < n-1:
                pages_dict[i] = (i, i+1)
    values_list = list(pages_dict.values())
    for i in range(1, len(values_list)):
        if i != 1:
            if p in values_list[i]:
                for key, value in pages_dict.items():
                    if values_list[i] == value:
                        front_count = key-1  # 3
                        back_count = int((n-front_count)/2)-1
                return min(front_count, back_count)
    return 0


print(pageCount(6, 2))
