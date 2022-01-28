import timeit

# Find the maximum value in a list
# input size changed to 1000000
def function1():
    lst = list(range(0, 1000000))
    # print(lst)
    maxi = lst[0]
    for i in lst:
        if i > maxi:
            maxi = i
    # print(maxi)

timeFunction1 = timeit.timeit(stmt="function1()", setup="from __main__ import function1", number=1)
print(f"time of the algorithm in Qst3.I of finding the max number in list {timeFunction1}")


# random list generator in range(0,60)
import random
randomlist3 = []
for i in range(0,1000000):
    n = random.randint(1,100)
    randomlist3.append(n)

# input list number in range(0,60)
def function3():
    randomlist3.sort()

timeFunction3 = timeit.timeit(stmt="function3()", setup="from __main__ import function3", number=1)
print(f"time of the algorithm in Qst3.III of finding the max number in a list {timeFunction3}")