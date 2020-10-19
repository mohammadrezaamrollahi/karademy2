import time
start = time.time()
def sumdigits(n):
    if n < 10:
        return n
    else:
        Sum = 0
        while n > 0:
            Sum += n % 10
            n //= 10
        n = Sum 
        return sumdigits(n) 

ones_counter = 0
twos_counter = 0
for number in range(1000):
    if sumdigits(number) == 1:
        ones_counter += 1
    elif sumdigits(number) == 2:
        twos_counter += 1

print("there is/are {} 1s and {} 2s".format(ones_counter, twos_counter))
print("Run Time: " + str( time.time() - start ))
