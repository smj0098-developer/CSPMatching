class Hall:
    def __init__(self, hallNumber: str):
        self.hallNumber: str = hallNumber
        self.hallName: str = "H" + str(self.hallNumber)
    domain: list[str] = []
