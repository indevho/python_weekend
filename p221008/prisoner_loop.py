import random
from re import I
N = 100
numbers = [i for i in range(100)]

random.shuffle(numbers)
summation = 0.0
for k in range(10000):
    random.shuffle(numbers)
    is_good = True
    for i in range(100):
        my_num = i
        is_flag = False
        for j in range(50):
            if numbers[my_num] == i:
                is_flag = True
                break
            my_num = numbers[my_num]
        if is_flag == False:
            is_good = False
            break
    if is_good == True:
        summation += 1.0
    print(summation / 10000.0)

