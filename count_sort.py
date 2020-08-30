from grapher import Plotter
import random

def count_sort(data, filename):
    plotter = Plotter("Count Sort")
    array = [0]*(max(data)+1)
    result = []
    plotter.plot(data,len(data)-1)
    for element in data:
        array[element] += 1

    for index, element in enumerate(array):
        if element != 0:
            result.append(index)
            plotter.plot(result,len(result)-1)

    plotter.animate(result,filename)

lis = list(range(1,15))
random.shuffle(lis)
count_sort(lis,"count.html")

