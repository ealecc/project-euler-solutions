'''What is the largest prime factor of the number 600851475143 ?'''

def factorise(num):
    '''yields prime factors of number num'''
    while num > 1:
        for i in range(2, num + 1):
            if num % i == 0:
                num //= i
                yield i
                break

def is_prime(num):
    '''test if num is a prime number'''
    if num < 2:
        return False
    if num == 2:
        return True

    # test if number is prime by testing modulus of all lower numbers
    for i in range(2, num):
        if num % i == 0:
            return False

    # if loop ends without returning, n is prime
    return True

def main():
    import sys

    # arg 0 is program name, arg 1 is desired number
    input = int(sys.argv[1])

    largest = 0

    for factor in factorise(input):
        if factor > largest and is_prime(factor):
            largest = factor

    print(largest)

main()