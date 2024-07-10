import math
def binary_search(array: list[int], value: int,  low: int, high: int, depth: int):
    print("Depth is: ")
    print(depth)
    mid = math.floor((low + (high - low) /2))
    # print("Mid is: ")
    # print(mid)
    result = False
    if value == mid:
        # print("Found Value")
        return True
    elif value > mid:
        low = mid
        result = binary_search(array, value, low, high, depth +1)
    elif value < mid:
        high = mid
        result =binary_search(array, value, low, high,  depth +1)
    else:
        return False
    return result
array = [0,1,2,3,4,5,6,7,8,9,10]
# print("Searching for value: 5")
# result = binary_search(array, 5, 0, len(array), 0)
# print("Result is: ")
# print(result)

print("Searching for value: 1")
result = binary_search(array, 1, 0, len(array)-1, 0)
print("Result is: ")
print(result)

print("Searching for value: 9")
result = binary_search(array, 9, 0, len(array)-1, 0)
print("Result is: ")
print(result)

print("Searching for value: 0")
result = binary_search(array, 0, 0, len(array)-1, 0)
print("Result is: ")
print(result)

