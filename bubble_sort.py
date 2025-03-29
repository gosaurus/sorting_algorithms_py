def get_lst_length(outer_lst_index: int, lst_to_check: int) -> int:
    """ Gets length of lst of check by subtracting away
    elements  already  checked"""
    length = len(lst)
    return length-index

lst = [104, 100, 86, 0, 1, 0, -23, -44, 56, 101]

# Set the condition for while loop to start
swaps_count = 1

while(swaps_count > 0):
    for index, element in enumerate(lst):

        # Reset swaps count after each loop
        swaps_count = 0
        
        for i in range(get_lst_length
            (outer_lst_index=index, lst_to_check=lst)-1):

            # If number in wrong order
            if lst[i] > lst[i+1]:
                temporary_element = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temporary_element

                # Increment swaps_count
                swaps_count += 1
                
        # Print lst after looping thrugh lst
        print(f'{lst}')
        
        # Confirm swaps_count
        print(f'swaps = {swaps_count}')

        if (swaps_count == 0):
            break
    
    print(f'Enumerate Suite swaps count = {swaps_count}')

print(f'sorted list = {lst}')