import timeit

#importing the timeit package that allows to esstimate the time it takes to run a certain algorithm
def mytime():
   myList = []
   for x in range(100):
       myList.append(x)


print(timeit.repeat(stmt="mytime()", setup="from __main__ import mytime", repeat=5, number=100))




