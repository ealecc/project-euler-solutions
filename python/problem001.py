'''Find the sum of all the multiples of 3 or 5 below 1000.'''

sum = 0

# sum multiples of 3 OR 5 below 1000
# multiples of 3 AND 5 need only be counted once
for i in range(0,1000):
    if (i % 3 == 0 or i % 5 == 0):
        sum += i

print(sum)