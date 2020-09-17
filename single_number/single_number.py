'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    temp = []

    # Loop over arr
    for i in arr:
        # Check to see if the index isnt in the temp list
        if i not in temp:
            # If it isnt, append in to temp list
            temp.append(i)
        else:
            # Otherwise, remove the index from temp
            temp.remove(i)
    return temp[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
