import time
start = time.time()
def sumdigits(n):
    if n < 10:
        return n
    else:
        Sum = 0
        digit_count = 0 # the variable to keep track the number of digits in the number
        while n > 0:
            digit_count += 1
            Sum += n % 10
            n //= 10
        n = Sum # main number update
        if digit_count > 1:
            return sumdigits(n) # recursion happens based on the condition

ones_counter = 0
twos_counter = 0

for number in range(1000):
    if sumdigits(number) == 1:
        print("1 : {}".format(number))
        ones_counter += 1
    elif sumdigits(number) == 2:
        print("2 : {}".format(number))
        twos_counter += 1

print("there is/are {} 1s and {} 2s".format(ones_counter, twos_counter))
print("Run Time: " + str( time.time() - start ))
