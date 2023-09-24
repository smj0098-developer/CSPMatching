import copy
from hall import *


class Problem:
    def __init__(self, constraintPairsList, groupsList, n, m):
        self.constraintPairsList = constraintPairsList
        self.groupsList = groupsList
        self.m = m
        self.n = n

    def backtracking(self, hallsList: list[Hall], assignmentList: list[tuple]):
        # the algorithm stops recursion as hallsList becomes empty
        selectedHall = self.MRV(hallsList)
        valuesToAssign = self.LCV(selectedHall.domain)

        for value in valuesToAssign:
            newHallList: list[Hall] = copy.deepcopy(hallsList)

            # Remove selectedHall from newHallList
            for hallToBeRemoved in newHallList:
                if hallToBeRemoved.hallNumber == selectedHall.hallNumber:
                    newHallList.remove(hallToBeRemoved)

            copiedAssignmentList = copy.deepcopy(assignmentList)
            copiedAssignmentList.append((selectedHall.hallNumber, value))

            self.forwardChecking(selectedHall, newHallList, value)

            if (len(copiedAssignmentList) == self.n):
                self.answerGenerator(copiedAssignmentList)
                raise Exception("stop")

            self.backtracking(newHallList, copiedAssignmentList)

    def MRV(self, hallsList) -> Hall:
        return min(
            hallsList, key=lambda x: len(x.domain))

    def LCV(self, hallDomain):
        # the first element in the tuple is the value itself and the second is how many preferences it has
        leastConstrainingValue = []
        for selectedGroupNumber in hallDomain:
            for group in self.groupsList:
                if str(group.groupNumber) == str(selectedGroupNumber):
                    leastConstrainingValue.append(
                        (selectedGroupNumber, len(group.preference)))
        leastConstrainingValue = sorted(
            leastConstrainingValue, key=lambda x: x[1], reverse=True)

        # Returns only group names
        return [x[0] for x in leastConstrainingValue]

    def forwardChecking(self, hall, copiedHallsList, valueToAssign):
        conflictList = []
        for tuple in self.constraintPairsList:
            if tuple[0].hallNumber == hall.hallNumber:
                conflictList.append(tuple[1].hallNumber)
            if tuple[1].hallNumber == hall.hallNumber:
                conflictList.append(tuple[0].hallNumber)
        for nominatedNeighboringHall in copiedHallsList:
            if nominatedNeighboringHall.hallNumber in conflictList:
                if valueToAssign in nominatedNeighboringHall.domain:
                    nominatedNeighboringHall.domain.remove(valueToAssign)

    def answerGenerator(self, finalAssignment):
        finalAssignment = sorted(finalAssignment, key=lambda x: int(x[0]))
        [print(i[1], end="") for i in finalAssignment]
