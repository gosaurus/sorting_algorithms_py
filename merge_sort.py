import math

lst = [6, 4, 3, 1, 2, 0, 7, 5]

def get_bisect_point(list_length: int) -> int:
    """Determine bisect point. Round down to nearest integer"""
    if list_length <= 1:
        return 1
    length = list_length/2
    print(f'half of length of {list_length} = {length}')
    return math.floor(length)

def recursively_bisect(working_list: list):
    """Bisects lists until length of list <= 1, then returns it to"""
    """left or right half, which is then sorted and merged"""
    if len(working_list) <= 1:
        print(f'working list = {working_list}')
        return working_list #base case...returns something like [6]

    bisect_point = get_bisect_point(len(working_list))
    print(f'working list before bisect = {working_list}')
    left = recursively_bisect(working_list[:bisect_point])
    right = recursively_bisect(working_list[bisect_point:])
    print(f'left = {left}, right={right}')

    return compare_and_merge(left, right)

def compare_and_merge(left, right):
    """While left AND right length have items, check each item in left"""
    """against corresponding item in right. Add if smaller. If no items left"""
    """in either one of the lists, it means other list is sorted and """
    """can be merged in"""
    merged_list = []
    while left and right: 
        if left[0] < right[0]:
            merged_list.append(left.pop(0))
        else:
            merged_list.append(right.pop(0))
    merged_list.extend(left)
    merged_list.extend(right)
    print(f'Merged list so far = {merged_list}')
    return merged_list

print(f'starting list {lst}, len = {len(lst)} \n')
lst_copy = lst[:]

nested_list = recursively_bisect(lst_copy)

print(f'{nested_list}')