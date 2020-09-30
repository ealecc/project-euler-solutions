'''By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''

sum = 0
fib1, fib2 = 0, 1
i = 0

while i < 4000000:
    # add even numbers to sum
    if (i % 2 == 0):
        sum += i
    
    # calculate next number in fibonacci sequence
    i = fib1 + fib2
    fib1 = fib2
    fib2 = i

print(sum)