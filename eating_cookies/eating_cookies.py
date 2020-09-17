'''
Input: an integer
Returns: an integer
'''

# Recursion should be effective


def eating_cookies(n, b=None):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        a = int(n - 1)
        b = int(n - 2)
        c = int(n - 3)
        return eating_cookies(a) + eating_cookies(b) + eating_cookies(c)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
