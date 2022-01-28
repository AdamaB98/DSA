import timeit

def mytime():
   myList = []
   for x in range(100):
       myList.append(x)


print(timeit.repeat(stmt="mytime()", setup="from __main__ import mytime", repeat=5, number=100))




