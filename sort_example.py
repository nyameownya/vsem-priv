def find_smallest(arr):
    smallest = arr[0] 
    smallestIndex= 0 
    for index in range(1,len(arr)):
        if arr[index] < smallest  : 
            smallest = arr[index]
            smallestIndex = index 
    return smallestIndex
def sort_by_smallest(arr):
    neoArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        neoArr.append(arr.pop(smallest))
    return neoArr

print(sort_by_smallest([5,2,4,3]))
