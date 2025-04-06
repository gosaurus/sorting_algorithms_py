import math

starting_lst = [6, 4, 3, 1, 0, 0, 7, 5]


def get_bisect_point(lst_length: int) -> int:
    """Determine bisect point. Round down to nearest integer"""
    if lst_length <= 1:
        return 1
    length = lst_length/2
    print(f'half of length of {lst_length} = {length}')
    return math.floor(length)


def recursively_bisect(working_lst: list):
    """Bisects lists until length of list <= 1, then returns it to"""
    """left or right half, which is then sorted and merged"""
    if len(working_lst) <= 1:
        print(f'working lst = {working_lst}')
        return working_lst
        # base case...returns something like [6]

    bisect_point = get_bisect_point(len(working_lst))
    print(f'working lst before bisect = {working_lst}')
    left = recursively_bisect(working_lst[:bisect_point])
    right = recursively_bisect(working_lst[bisect_point:])
    print(f'left = {left}, right={right}')

    return compare_and_merge(left, right)


def compare_and_merge(left: list, right: list) -> list:
    """While left AND right length have items, check each item in left"""
    """against corresponding item in right. Add if smaller. If no items left"""
    """in either one of the lists, it means other list is sorted and """
    """can be merged in"""
    merged_lst = []
    while left and right:
        if left[0] < right[0]:
            merged_lst.append(left.pop(0))
        else:
            merged_lst.append(right.pop(0))
    merged_lst.extend(left)
    merged_lst.extend(right)
    print(f'Merged lst so far = {merged_lst}')
    return merged_lst


print(f'starting list {starting_lst}, len = {len(starting_lst)} \n')
lst_copy = starting_lst[:]

nested_list = recursively_bisect(lst_copy)

print(f'{nested_list}')
