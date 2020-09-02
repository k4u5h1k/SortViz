from grapher import Plotter

class CocktailSort():
    def __init__(self,data,filename):
        self.test = Plotter("Cocktail Sort")
        self.data = data
        self.cocktailSort(len(self.data)-1)
        self.test.animate(self.data,filename)
    
    def cocktailSort(self,n): 
       
        swapped = True
        
        while (swapped == True): 
            swapped = False
            start=0
            for i in range (start, n): 
                if (self.data[i] > self.data[i + 1]) : 
                    
                    swapped = True
                    self.test.plot(self.data,i+1,i)
                    self.data[i],self.data[i+1] = self.data[i+1],self.data[i] 
                    self.test.plot(self.data,i,i+1)
            if (swapped == False): 
                break
            swapped = False
            n = n-1
            for i in range(n-1, start-1, -1): 
                if (self.data[i] > self.data[i + 1]): 
                        
                        swapped = True
                        self.test.plot(self.data,i+1,i)
                        self.data[i],self.data[i+1] = self.data[i+1],self.data[i] 
                        self.test.plot(self.data,i,i+1)
                start = start + 1

