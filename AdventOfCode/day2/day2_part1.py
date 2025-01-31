import numpy as np

listOfReports = []

with open('day2_input.txt', 'r') as file:
    for line in file:
        listOfReports.append([int(x) for x in line.strip("\n").split(" ")])

# Test data for debugging
# testListOfReports = [[7, 6, 4, 2, 1],
#                      [1, 2, 7, 8, 9],
#                      [9, 7, 6, 2, 1],
#                      [1, 3, 2, 4, 5],
#                      [8, 6, 4, 4, 1],
#                      [1, 3, 6, 7, 9]]
# listOfReports = testListOfReports

# def checkIncreasing(report):
#     for i in range(len(report) - 1):
#         if not (report[i+1] - report[i] > 0 and report[i+1] - report[i] <= 3):
#             return i  # Return the index of failure
#     return -1  # Return -1 if no issue

# def checkDecreasing(report):
#     for i in range(len(report) - 1):
#         if not (report[i+1] - report[i] < 0 and report[i+1] - report[i] >= -3):
#             return i  # Return the index of failure
#     return -1  # Return -1 if no issue

# numSafe = 0

# for report in listOfReports:
#     increasing = (report[1] - report[0] > 0)

#     if increasing:
#         errorIdx = checkIncreasing(report)
#         if errorIdx == -1:
#             numSafe += 1
#         else:
#             # Attempt to remove one item at a time and check if it becomes safe
#             for i in range(len(report)):
#                 rep1 = report[:i] + report[i+1:]  # Remove item at index i without using pop
#                 if checkIncreasing(rep1) == -1:
#                     numSafe += 1
#                     break  # Exit after first successful fix
#     else:
#         errorIdx = checkDecreasing(report)
#         if errorIdx == -1:
#             numSafe += 1
#         else:
#             # Attempt to remove one item at a time and check if it becomes safe
#             for i in range(len(report)):
#                 rep1 = report[:i] + report[i+1:]  # Remove item at index i without using pop
#                 if checkDecreasing(rep1) == -1:
#                     numSafe += 1
#                     break  # Exit after first successful fix

# print(numSafe)


# def is_safe(row):
#     inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
#     if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
#         return True
#     return False

# data = [[int(y) for y in x.split(' ')] for x in open('02.txt').read().split('\n')]

# safe_count = sum([is_safe(row) for row in data])
# print(safe_count)

# safe_count = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data])
# print(safe_count)