class Group:
    def __init__(self, groupNumber, preference):
        self.groupNumber = groupNumber
        self.groupName = "G" + str(self.groupNumber)
        self.preference = preference
