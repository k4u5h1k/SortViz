from grapher import Plotter

class BucketSort():
	def __init__(self,data,filename):
            self.plotter=Plotter("Bucket Sort")
            self.plotter.animate(self.bucket(data,filename),filename)

	def insertionSort(self,arr,b,filename):
	    arr2 = []
	    for i in range(len(arr)):
	        if i == b:
	            k=len(arr2)
	        for j in arr[i]:
	            arr2.append(j)
	            
	    for i in range(1,len(arr[b])): 
	        up = arr[b][i] 
	        j = i - 1
	        while j >=0 and arr[b][j] > up:
	            self.plotter.plot(arr2,k+j+1,k+j)
	            arr2[k+j+1]=arr2[k+j]
	            arr2[k+j]=up
	            arr[b][j + 1] = arr[b][j]
	            arr[b][j]=up
	            self.plotter.plot(arr2,k+j,k+j+1)
	            j -= 1
	        arr[b][j + 1] = up
	    return arr[b],arr2
	              
	def bucket(self,x,filename):
            arr = []
            arr2 = []
            arr3=[]

            x = list(map(lambda a:a/100,x))

            slot_num = 10  
            for i in range(slot_num):
               arr.append([]) 
                  
            for j in x: 
                index_b = int(slot_num * j)  
                arr[index_b].append(j) 

            self.plotter.plot(x,0)
              
            for i in arr:
                if len(i)!=0:
                    arr2.append(i)
                   
            for i in range(len(arr2)): 
                arr2[i],arr3 = self.insertionSort(arr2,i,filename) 

            return arr3
