from grapher import Plotter
import random

def insertion_sort(data, filename):
    test = Plotter("Insertion Sort")

    for i in range(len(data)):
        temp = data[i]
        j = i-1
        while  j >=0 and temp < data[j]:
            #I want to show the graph with index j+1 highlighted green and j+1 red
            test.plot(data,j+1,j)

            data[j+1] = data[j]
            data[j] = temp

            #After swapping I want to show the graph with index j highlighted red and j+1 green
            test.plot(data,j,j+1)

            j -= 1

        data[j+1] = temp

    test.animate(data,filename)

