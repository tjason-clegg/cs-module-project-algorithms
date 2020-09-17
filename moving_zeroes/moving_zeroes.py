'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    rtn = []
    for i in arr:
        # If it comes across a 0, append it to the rtn list
        if i == 0:
            rtn.append(i)
        else:
            # If it doesnt, insert a 0, as well as the index of the 0
            rtn.insert(0, i)
    return rtn


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
