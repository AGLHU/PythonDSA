# O(n^2)
def findSmallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selectionSort(array):
    newArray = []
    for i in range(len(array)):
        smallest = findSmallest(array)
        newArray.append(array.pop(smallest))
    return newArray

print(selectionSort([61, 34, 72, 99, -12, 100]))