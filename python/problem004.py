'''Find the largest palindrome made from the product of two 3-digit numbers.'''

def is_palindrome(num):
    '''test if a number is a palindrome'''
    num_string = str(num)
    reversed_string = reversed(num_string)

    if list(num_string) == list(reversed_string):
        return True
    else:
        return False

def generate_products():
    '''generate the product of three-digit numbers'''
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            print(i, '*', j)
            yield i * j

def main():
    for product in generate_products():
        if is_palindrome(product):
            print(product)
            return 1

main()
    