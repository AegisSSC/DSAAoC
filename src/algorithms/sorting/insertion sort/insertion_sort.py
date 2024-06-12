
matrix_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
matrix_b = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]


# The goal of insertion sort is to, one element at a time, sort it into place. It makes it's comparison one element at a time progressively working it's way to the front of the list. 
# !TODO: Expand to include handling negative numbers


def insertion_sort(matrix):
    print("The Matrix before Insertion Sorting is: ")
    print(matrix)


    for j in range(1, len(matrix)):
        key = matrix[j]
        i = j-1
        while i >= 0 and matrix[i] > key:
            matrix[i+1] = matrix[i]
            i -= 1
        matrix[i+1]=key
    print("The Resulting matrix after Insertion Sorting is: ")
    print(matrix)

insertion_sort(matrix_b)