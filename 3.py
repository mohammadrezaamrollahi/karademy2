import time
start = time.time()
def digit_adder(number):
    if number < 10 :
        return number
    else:
        string_number=str(number)
        sum_up=0
        for item in string_number:
            sum_up += int(item)
        return digit_adder(sum_up) 

def zero_one_digit_counter(start , stop):
    list1=[]
    list2=[]
    for number in range(start , stop):
        if digit_adder(number)==1:
            list1.append(number)
        elif digit_adder(number)==2:
            list2.append(number)
    return len(list1) , len(list2)

f1=zero_one_digit_counter(0,1000)
print(f1)
print("Run Time: " + str( time.time() - start ))
