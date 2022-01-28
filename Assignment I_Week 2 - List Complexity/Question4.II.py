import timeit
from matplotlib import pyplot as plt

# maximum value in a list
functionList = []
timeList = []


# input string length (0-30)
def function1():
    inputString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
                  " Maecenas pretium quam id diam porta, " \
                  "ac hendrerit elit rutrum. Quisque ultrices tincidunt velit, \
                  at molestie turpis rutrum sit amet."

    inputString.lower()

timeFunction1 = timeit.timeit(stmt="function1()", setup="from __main__ import function1", number=1)
timeList.append(timeFunction1)
functionList.append("range(0-200)")


# print(timeFunction1)


def function2():
    inputString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
                  " Maecenas pretium quam id diam porta, " \
                  "ac hendrerit elit rutrum. Quisque ultrices tincidunt velit, \
                  at molestie turpis rutrum sit amet.Pellentesque habitant morbi tristique senectus et netus" \
                  " et malesuada fames ac turpis egestas. Donec sollicitudin, " \
                  "magna nec convallis aliquam, orci eros efficitur tortor, " \
                  " et malesuada fames ac turpis egestas. Donec sollicitudin, "
    inputString.lower()

timeFunction2 = timeit.timeit(stmt="function2()", setup="from __main__ import function2", number=1)
timeList.append(timeFunction2)
functionList.append("range(0-400)")


# print(timeFunction2)

def function3():
    inputString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
                  " Maecenas pretium quam id diam porta, " \
                  "ac hendrerit elit rutrum. Quisque ultrices tincidunt velit, \
                  at molestie turpis rutrum sit amet.Pellentesque habitant morbi tristique senectus et netus" \
                  " et malesuada fames ac turpis egestas. Donec sollicitudin, " \
                  "magna nec convallis aliquam, orci eros efficitur tortor, et lacinia risus est et nisi." \
                    "magna nec convallis aliquam, orci eros efficitur tortor, " \
                    " et malesuada fames ac turpis egestas. Donec sollicitudin" \
                    "magna nec convallis aliquam, orci eros efficitur tortor, " \
                    " et malesuada fames ac turpis egestas. Donec sollicitudin, "
    inputString.lower()


timeFunction3 = timeit.timeit(stmt="function3()", setup="from __main__ import function3", number=1)
timeList.append(timeFunction3)
functionList.append("range(0-600)")
# print(timeFunction3)

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
