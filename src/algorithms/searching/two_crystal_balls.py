import math

def two_crystal_ball(breaks: list[bool]):
    total_Iterations = int(0)
    jump_Amount = math.floor(math.sqrt(len(breaks)))
    # print("The Jump amount is: " + str(jump_Amount))
    for i in range(jump_Amount, len(breaks)+1, jump_Amount):
        total_Iterations +=1
        # print("Iterations = " + str(total_Iterations))
        # print("I = " + str(i))
        if breaks[i-1]:
            print("Ball 1 Broke on floor: " + str(i))
            break;
    i -= jump_Amount
    j = int(0) 
    while(j <= jump_Amount and i < len(breaks)):
        total_Iterations +=1
        # print("Iterations = " + str(total_Iterations))
        # print("I = " + str(i))
        if breaks[i]:
            print("Ball 2 broke on floor: " + str(i+1))
            
            return i+1, total_Iterations
        j +=1
        i +=1


array = [False, False, False, False, False, False, False, False, True]
result = two_crystal_ball(array)
print("The ball broke on floor " + str(result[0]))
print("The Total Iterations was: " + str(result[1]))


array = [False, False, True, True, True, True, True, True, True]
result = two_crystal_ball(array)
print("The ball broke on floor " + str(result[0]))
print("The Total Iterations was: " + str(result[1]))

array = [False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, True]
result = two_crystal_ball(array)
print("The ball broke on floor" + str(result[0]))
print("The Total Iterations was: " + str(result[1]))

array = [False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False,
         False, False, True, True, True, True, True, True, True,]
result = two_crystal_ball(array)
print("The ball broke on floor "  + str(result[0]))
print("The Total Iterations was: " + str(result[1]))

array = [False, True, True, True, True, True, True, True, True,
         True, True, True, True, True, True, True, True, True,
         True, True, True, True, True, True, True, True, True,
         True, True, True, True, True, True, True, True, True,
         True, True, True, True, True, True, True, True, True,
         True, True, True, True, True, True, True, True, True,
         True, True, True, True, True, True, True, True, True,
         True, True, True, True, True, True, True, True, True,
         True, True, True, True, True, True, True, True, True,]
result = two_crystal_ball(array)
print("The ball broke on floor "  + str(result[0]))
print("The Total Iterations was: " + str(result[1]))