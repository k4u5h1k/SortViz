from algos.insertion_sort import insertion_sort
from algos.bubble_sort import bubble_sort
from algos.quick_sort import QuickSort

def function_names():
    return {
            'bubble' : bubble_sort,
            'quick' : QuickSort,
            'insertion' : insertion_sort
            }

def pretty_names():
    return {
            'bubble' :  'Bubble Sort',
            'quick' : 'Quick Sort',
            'insertion' : 'Insertion Sort',
            }

def filenames():
    return {
            'bubble' : 'bubblesort.html',
            'quick' : 'quicksort.html',
            'insertion' : 'insertionsort.html'
            }
