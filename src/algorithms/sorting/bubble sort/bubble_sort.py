

def swap(A, B):
    temp = A
    A = B
    B = temp

def bubble_sort(array: list[int]):
    print("Starting array is:")
    print(array)
    n = len(array)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    print("Finished Sorting. Array is now:")
    print(array)
    




array = [10,9,8,7,6,5,4,3,2,1,0]
bubble_sort(array)

