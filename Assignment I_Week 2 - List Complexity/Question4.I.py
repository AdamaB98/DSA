import timeit
from matplotlib import pyplot as plt

# maximum value in a list
functionList = []
timeList = []

# input size (0-30)
def function1():
    lst = list(range(0, 30))
    # print(lst)
    maxi = lst[0]
    for i in lst:
        if i > maxi:
            maxi = i
    print(maxi)

timeFunction1 = timeit.timeit(stmt="function1()", setup="from __main__ import function1", number=1)
timeList.append(timeFunction1)
functionList.append("f1")
# print(timeFunction1)
# input size (0- 60)
def function2():
    lst = list(range(0, 60))
    # print(lst)
    maxi = lst[0]
    for i in lst:
        if i > maxi:
            maxi = i
    print(maxi)

timeFunction2 = timeit.timeit(stmt="function2()", setup="from __main__ import function2", number=1)
timeList.append(timeFunction2)
functionList.append("f2")
print(timeFunction2)
# input size (0-100)
def function3():
    lst = list(range(0, 100))
    # print(lst)
    maxi = lst[0]
    for i in lst:
        if i > maxi:
            maxi = i
    print(maxi)

timeFunction3 = timeit.timeit(stmt="function3()", setup="from __main__ import function3", number=1)
timeList.append(timeFunction3)
functionList.append("f3")


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