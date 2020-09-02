from grapher import Plotter
import random

def cycle_sort(data,filename): 
  test=Plotter("Cycle Sort")    

  for cycleStart in range(0, len(data) - 1): 
    item = data[cycleStart] 
    
    pos = cycleStart 
    for i in range(cycleStart + 1, len(data)): 
      if data[i] < item: 
        pos += 1
     
    if pos == cycleStart: 
      continue

    while item == data[pos]: 
      pos += 1
    data[pos], item = item, data[pos] 
    test.plot(data,pos,cycleStart)  

    while pos != cycleStart: 
      pos = cycleStart 
      for i in range(cycleStart + 1, len(data)): 
        if data[i] < item: 
          pos += 1
 
      while item == data[pos]: 
        pos += 1
      data[pos], item = item, data[pos] 
      test.plot(data,cycleStart,pos)
    
  test.animate(data,filename)
