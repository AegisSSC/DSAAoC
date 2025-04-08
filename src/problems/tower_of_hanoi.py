# The Tower of Hanoi is a famous problem which was posed by a French mathematician in 1883.
# What you need to do is move all the disks from the left hand post to the right hand post. 
# You can only move the disks one at a time and you can never place a bigger disk on a smaller disk.

# The aim is to try and complete the transfer using the smallest number of moves possible. 
# For example if you have three disks, the minimum number of moves is 7. 
# If you have four disks, the minimum number of moves is 15. 
# Can you complete the problem in the smallest number of moves possible?

# Try it out here.

# The posts can be represented using a stack. In Python we can create a stack like behavior using a list.
# We will use the pop() and the append() functions to get this behavior
# To enforce the original rule, 
# we can create a conditional that the number cannot move to somewhere that is larger than the number currently on the stack. 

postA = [6, 5, 4, 3, 2, 1]
postB = [] 
postC = []

# Print all of the posts:
print(postA)
print(postB)
print(postC)

# Start with the first step.
# Take the top disk and move it to postB
disk = postA.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)

# It should now look like:
# postA = [6, 5, 4, 3, 2]
# postB = [1] 
# postC = []

# Second Step, take the next disk and move it to postC. 
# It has to go to postC since the disk is bigger than the value at postB
disk = postA.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)

# It should now look like:
# postA = [6, 5, 4, 3]
# postB = [1] 
# postC = [2]

# Third Step, since there is not a spot for the next disk on postA
# Move to Post B and see if you can place it onto postC.
# You can do this since the disk in postB is smaller than postC
disk = postB.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)

# It should now look like:
# postA = [6, 5, 4, 3]
# postB = [] 
# postC = [2, 1]

#Fourth Step, move the next disk from postA to postB
disk = postA.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)

# It should now look like:
# postA = [6, 5, 4]
# postB = [3] 
# postC = [2, 1]


# Fifth Step, since there is not a spot for the next disk on postA
# Move to Post B and see if you can place it onto postC.
# Since you cannot move the disk from postB onto postC,
# See if you can move a disk from postC to postA. 
disk = postC.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)

# It should now look like:
# postA = [6, 5, 4, 1]
# postB = [3] 
# postC = [2]

# Sixth Step,
# Move the disk from postC to postB
# This can be done since the disk on postC is smaller than postB
disk = postC.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 5, 4, 1]
# postB = [3, 2] 
# postC = []


# Seventh Step,
# Move the Disk at postA onto postB
disk = postA.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 5, 4]
# postB = [3, 2, 1] 
# postC = []

# Eighth Step,
# Move the Disk at postA to postC
disk = postA.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 5]
# postB = [3, 2, 1] 
# postC = [4]

# Move the disk from PostB to PostC
disk = postB.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 5]
# postB = [3, 2] 
# postC = [4,1]

# Move disk from postB to postA 
disk = postB.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 5, 2]
# postB = [3] 
# postC = [4,1]

# Move disk from postC to postA
disk = postC.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 5, 2, 1]
# postB = [3] 
# postC = [4]

# Move disk from postB to postC
disk = postB.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 5, 2, 1]
# postB = [] 
# postC = [4, 3]

# Move disk from postA to postB
disk = postA.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 5, 2]
# postB = [1] 
# postC = [4, 3]

# Move disk from postA to postC 
disk = postA.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 5]
# postB = [1] 
# postC = [4, 3, 2]

# Move disk from postB to PostC 
disk = postB.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 5]
# postB = [] 
# postC = [4, 3, 2, 1]

# Move disk from postA to PostB 
disk = postA.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6]
# postB = [5] 
# postC = [4, 3, 2, 1]


# Move disk from postC to PostA 
disk = postC.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 1]
# postB = [5] 
# postC = [4, 3, 2]


# Move disk from postC to PostB 
disk = postC.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 1]
# postB = [5, 2] 
# postC = [4, 3]

# Move disk from postA to PostB 
disk = postA.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6]
# postB = [5, 2, 1] 
# postC = [4, 3]

# Move disk from postC to PostA 
disk = postC.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 3]
# postB = [5, 2, 1] 
# postC = [4]

# Move disk from postB to PostC 
disk = postB.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 3]
# postB = [5, 2] 
# postC = [4, 1]


# Move disk from postB to PostA 
disk = postB.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 3, 2]
# postB = [5] 
# postC = [4, 1]

# Move disk from postC to PostA 
disk = postC.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 3, 2, 1]
# postB = [5] 
# postC = [4]

# Move disk from postC to PostB 
disk = postC.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 3, 2, 1]
# postB = [5, 4] 
# postC = []


# Move disk from postA to PostB 
disk = postA.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 3, 2]
# postB = [5, 4, 1] 
# postC = []


# Move disk from postA to PostC 
disk = postA.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 3]
# postB = [5, 4, 1] 
# postC = [2]

# Move disk from postB to PostC 
disk = postB.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 3]
# postB = [5, 4] 
# postC = [2, 1]

# Move disk from postA to PostB 
disk = postA.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6]
# postB = [5, 4, 3] 
# postC = [2, 1]

# Move disk from postC to PostA 
disk = postC.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 1]
# postB = [5, 4, 3] 
# postC = [2]


# Move disk from postC to PostB 
disk = postC.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6, 1]
# postB = [5, 4, 3, 2] 
# postC = []

# Move disk from postA to PostB 
disk = postA.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [6]
# postB = [5, 4, 3, 2, 1] 
# postC = []


# Move disk from postA to PostC 
disk = postA.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = []
# postB = [5, 4, 3, 2, 1] 
# postC = [6]


# Move disk from postB to PostC 
disk = postB.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = []
# postB = [5, 4, 3, 2] 
# postC = [6, 1]

# Move disk from postB to PostA 
disk = postB.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [2]
# postB = [5, 4, 3] 
# postC = [6, 1]

# Move disk from postC to PostA 
disk = postC.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [2, 1]
# postB = [5, 4, 3] 
# postC = [6]

# Move disk from postB to PostC 
disk = postB.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [2, 1]
# postB = [5, 4] 
# postC = [6, 3]

# Move disk from postA to postB 
disk = postA.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [2]
# postB = [5, 4, 1] 
# postC = [6, 3]


# Move disk from postA to postC 
disk = postA.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = []
# postB = [5, 4, 1] 
# postC = [6, 3, 2]

# Move disk from postB to postC 
disk = postB.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = []
# postB = [5, 4] 
# postC = [6, 3, 2, 1]

# Move disk from postB to postA 
disk = postB.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [4]
# postB = [5] 
# postC = [6, 3, 2, 1]


# Move disk from postC to postA 
disk = postC.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [4, 1]
# postB = [5] 
# postC = [6, 3, 2]

# Move disk from postC to postB 
disk = postC.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [4, 1]
# postB = [5, 2] 
# postC = [6, 3]

# Move disk from postA to postB 
disk = postA.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [4]
# postB = [5, 2, 1] 
# postC = [6, 3]

# Move disk from postC to postA 
disk = postC.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [4,3]
# postB = [5, 2, 1] 
# postC = [6]

# Move disk from postB to postC 
disk = postB.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [4,3]
# postB = [5, 2] 
# postC = [6, 1]

# Move disk from postB to postA 
disk = postB.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [4, 3, 2]
# postB = [5] 
# postC = [6, 1]


# Move disk from postC to postA 
disk = postC.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [4, 3, 2, 1]
# postB = [5] 
# postC = [6]


# Move disk from postB to postC 
disk = postB.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [4, 3, 2, 1]
# postB = [] 
# postC = [6, 5]

# Move disk from postA to postB 
disk = postA.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [4, 3, 2]
# postB = [1] 
# postC = [6, 5]

# Move disk from postA to postC 
disk = postA.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [4, 3, 2]
# postB = [1] 
# postC = [6, 5, 2]

# Move disk from postB to postC 
disk = postB.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [4, 3]
# postB = [] 
# postC = [6, 5, 2, 1]

# Move disk from postA to postB 
disk = postA.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [4]
# postB = [3] 
# postC = [6, 5, 2, 1]

# Move disk from postC to postA 
disk = postC.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [4, 1]
# postB = [3] 
# postC = [6, 5, 2]


# Move disk from postC to postB 
disk = postC.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [4, 1]
# postB = [3, 2] 
# postC = [6, 5]

# Move disk from postA to postB 
disk = postA.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [4]
# postB = [3, 2, 1] 
# postC = [6, 5]


# Move disk from postA to postC 
disk = postA.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = []
# postB = [3, 2, 1] 
# postC = [6, 5, 4]


# Move disk from postB to postC 
disk = postB.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = []
# postB = [3, 2] 
# postC = [6, 5, 4, 1]

# Move disk from postB to postA 
disk = postB.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [2]
# postB = [3] 
# postC = [6, 5, 4, 1]

# Move disk from postC to postA 
disk = postC.pop()
postA.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [2, 1]
# postB = [3] 
# postC = [6, 5, 4]

# Move disk from postB to postC 
disk = postB.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [2, 1]
# postB = [] 
# postC = [6, 5, 4, 3]


# Move disk from postA to postB 
disk = postA.pop()
postB.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = [2]
# postB = [1] 
# postC = [6, 5, 4, 3]


# Move disk from postA to postC 
disk = postA.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = []
# postB = [1] 
# postC = [6, 5, 4, 3, 2]


# Move disk from postB to postC 
disk = postB.pop()
postC.append(disk)
print(postA)
print(postB)
print(postC)
# It should now look like:
# postA = []
# postB = [] 
# postC = [6, 5, 4, 3, 2, 1]

print("Done!")
# Print all of the posts:
print(postA)
print(postB)
print(postC)