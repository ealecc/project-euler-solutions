'''What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?'''

import sys

def is_divisible_by_range(num, low, high):
    '''test whether num is divisible by all numbers in cases array'''

    for case in range(low, high):
        if num % case != 0:
            return False

    return True

def main():
    #get CLI arguments
    if len(sys.argv) != 3:
        return 1
    low = int(sys.argv[1])
    high = int(sys.argv[2])

    # find smallest number divisible by range between inputs
    i = high
    while True:
        print(i)
        if is_divisible_by_range(i, low, high):
            break
        # target number will always be divisible by high
        # therefore, increment by high to reduce test cases
        i += high

    print(i)

main()
