#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    # validate if n > 1 and ar > 1
    if n < 1 or len(ar) < 1:
        return 0
    # create a dict to store the count of each color sock
    sock_color_count = {}
    for color in ar:
        if sock_color_count.get(color) is None:
            sock_color_count[color] = 1
        else:
            sock_color_count[color] += 1
    # get the values of dict and count the number of pairs
    color_count_list = sock_color_count.values()
    no_of_pairs = 0
    for count in color_count_list:
        if count >= 2:
            no_of_pairs += int(count/2)
    return no_of_pairs


# print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
print(sockMerchant(15, [6, 5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5]))
