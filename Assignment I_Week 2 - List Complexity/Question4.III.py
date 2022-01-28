import timeit
from matplotlib import pyplot as plt

# maximum value in a list
functionList = []
timeList = []

# random list generator
import random
randomlist = []
for i in range(0,30):
    n = random.randint(1,100)
    randomlist.append(n)


# input list number in range(0,30)
def function1():
    randomlist.sort()

timeFunction1 = timeit.timeit(stmt="function1()", setup="from __main__ import function1", number=1)
timeList.append(timeFunction1)
functionList.append("range(0-30)")
# print(timeFunction1)

# random list generator in range(0,60)
import random
randomlist2 = []
for i in range(0,60):
    n = random.randint(1,100)
    randomlist2.append(n)


# input list number in range(0,60)
def function2():
    randomlist2.sort()

timeFunction2 = timeit.timeit(stmt="function2()", setup="from __main__ import function2", number=1)
timeList.append(timeFunction2)
functionList.append("range(0-60)")
# print(timeFunction2)


# random list generator in range(0,60)
import random
randomlist3 = []
for i in range(0,100):
    n = random.randint(1,100)
    randomlist3.append(n)


# input list number in range(0,60)
def function3():
    randomlist3.sort()

timeFunction3 = timeit.timeit(stmt="function3()", setup="from __main__ import function3", number=1)
timeList.append(timeFunction3)
functionList.append("range(0-100)")
print(timeFunction3)


# plotting time to run each function with its function operation
x_values = timeList
y_values = functionList
print(x_values)
print(y_values)

plt.title("graph of time verses space of an algoritm")
plt.xlabel("run time")
plt.ylabel("input size")

plt.plot(x_values, y_values)
plt.show()
