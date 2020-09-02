from grapher import Plotter

class CycleSort():
    def __init__(self,data,filename):
        self.plotter = Plotter("Cycle Sort")
        self.plotter.animate(self.cycle_sort(data),filename)

    def cycle_sort(self,data): 
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
        self.plotter.plot(data,pos,cycleStart)  

        while pos != cycleStart: 
          pos = cycleStart 
          for i in range(cycleStart + 1, len(data)): 
            if data[i] < item: 
              pos += 1
     
          while item == data[pos]: 
            pos += 1
          data[pos], item = item, data[pos] 
          self.plotter.plot(data,cycleStart,pos)

      return data
        
