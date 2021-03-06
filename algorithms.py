from algos.insertion_sort import InsertionSort
from algos.bubble_sort import BubbleSort
from algos.quick_sort import QuickSort
from algos.merge_sort import MergeSort
from algos.count_sort import CountSort
from algos.cocktail_sort import CocktailSort
from algos.comb_sort import CombSort
from algos.heap_sort import HeapSort
from algos.cycle_sort import CycleSort
from algos.stooge_sort import StoogeSort
from algos.gnome_sort import GnomeSort
from algos.selection_sort import SelectionSort
from algos.pigeonhole_sort import PigeonholeSort
from algos.pancake_sort import PancakeSort

#DOUBLE CHECK THAT THE KEYS ARE SAME IN ALL DICTS

def function_names(): # for calling from the web.py loop
    return {
            'bubble' : BubbleSort,
            'quick' : QuickSort,
            'insertion' : InsertionSort,
            'merge' : MergeSort,
            'count' : CountSort,
            'cocktail' : CocktailSort,
            'comb' : CombSort,
            'heap' : HeapSort,
            'cycle' : CycleSort,
            'stooge' : StoogeSort,
            'gnome' : GnomeSort,
            'selection' : SelectionSort,
            'pancake' : PancakeSort,
            'pigeonhole' : PigeonholeSort
            }

def pretty_names(): # to show in the index menu checkbox options
    return {
            'bubble' :  'Bubble Sort',
            'quick' : 'Quick Sort',
            'insertion' : 'Insertion Sort',
            'merge' : 'Merge Sort',
            'count' : 'Count Sort',
            'cocktail' : 'Cocktail Sort',
            'comb' : 'Comb Sort',
            'heap' : 'Heap Sort',
            'cycle' : 'Cycle Sort',
            'stooge' : 'Stooge Sort',
            'gnome' : 'Gnome Sort',
            'selection' : 'Selection Sort',
            'pancake' : 'Pancake Sort',
            'pigeonhole' : 'Pigeonhole Sort'
            }

def filenames(): # inside algos directory
    return {
            'bubble' : 'bubblesort.html',
            'quick' : 'quicksort.html',
            'insertion' : 'insertionsort.html',
            'merge' : 'mergesort.html',
            'count' : 'countsort.html',
            'cocktail' : 'cocktailsort.html',
            'comb' : 'combsort.html',
            'heap' : 'heapsort.html',
            'cycle' : 'cyclesort.html',
            'stooge' : 'stoogesort.html',
            'gnome' : 'gnomesort.html',
            'selection' : 'selectionsort.html',
            'pancake' : 'pancakesort.html',
            'pigeonhole' : 'pigeonholesort.html'
            }
