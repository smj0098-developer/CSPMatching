from hall import *
from problem import *
from group import *
from ac3 import *
import copy

# n: Number of Halls
# m: Number of Groups
n, m = input().split(" ")
m = int(m)
n = int(n)
hallsList = []
shouldRunAC3 = True

# creating all halls with their hallNumber
for i in range(n):
    hallsList.append(Hall(str(i+1)))

groupsList = []
# adding groups to halls' domains according to each group's preference
for groupIndex in range(1, m+1):
    preferenceLineList = input().split(" ")
    groupsList.append(Group(groupIndex, preferenceLineList))
    for groupHallNumber in preferenceLineList:
        for hall in hallsList:
            if hall.hallNumber == groupHallNumber:
                previousDomain = copy.deepcopy(hall.domain)
                previousDomain += [str(groupIndex)]
                hall.domain = previousDomain

# creating a list of pairs of variables that cannot have same values
constraintPairsList = []
numberOfConflicts = int(input())
for i in range(numberOfConflicts):
    pairOfHallsInConflict = input().split(" ")
    x1 = hallsList[int(pairOfHallsInConflict[0])-1]
    x2 = hallsList[int(pairOfHallsInConflict[1])-1]
    conflictTuple = (x1, x2)
    constraintPairsList.append(conflictTuple)

# [print("domain of hall ", a.hallNumber, a.domain) for a in hallsList]

# Run AC3
if (shouldRunAC3):
    constraintPairsList = [i for i in constraintPairsList]
    for i in range(numberOfConflicts):
        conflict = constraintPairsList[i]
        constraintPairsList.append((conflict[1], conflict[0]))

    if (AC3(constraintPairsList) == False):
        print("No")
        exit()

# print("After Running AC3 -----------")
# [print("domain of hall ", a.hallNumber, a.domain) for a in hallsList]

problem = Problem(constraintPairsList, groupsList, n, m)
try:
    problem.backtracking(hallsList, list())
    print("No")

except:
    pass
