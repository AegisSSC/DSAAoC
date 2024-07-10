
def linear_search(haystack: list[int], needle: int):
    for i in range(0,len(haystack)):
        if (haystack[i] == needle):
            return True 
    return False

array = [1,2,3,4,5,6,7,8,9,10]
print(array)
result = linear_search(array, 9)
print("The result of the function is: ")
print(result)

array = [2,4,6,8,10,1,3,5,7,9]
print(array)
result = linear_search(array, 7)
print("The result of the function is: ")
print(result)

