import numpy as np

readList1 = []
readList2 = []

freqMap = {}

# Open the file in read mode
with open('day1_input.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # print(line)
        nums = line.split("   ")
        # Print each line
        readList1.append(int(nums[0]))

        if not (int(nums[0]) in freqMap):
            freqMap[int(nums[0])] = 0

        readList2.append(int(nums[1]))

# print(len(readList1), len(readList2))

list1 = np.sort( np.array(readList1), axis=0)
list2 = np.sort( np.array(readList2), axis=0)

# distance = 0

for i in range(0, len(list1)):
    if list2[i] in freqMap:
        freqMap[list2[i]] += 1

newDist = 0

for key, val in freqMap.items():
    newDist += key*val

print(newDist)