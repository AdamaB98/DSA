from memory_profiler import *
import numpy
# we will find the memory space of our function in python


@profile
def memory():
    new = list(range(100))
    num = numpy.array([range(1000000)])
    newlist = list(range(200000))
    a = [1] * (100000 ** 1)
    print(a)
    b = [2] * (30000000 * 10 ** 2)
    pass


# print(memory())
if __name__ == "__main__":
    memory()


