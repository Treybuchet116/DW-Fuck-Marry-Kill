class Character:
    def __init__(self, charID, charName, nine, ten, eleven, twelve, thirteen, TW, SJA, imagePath, fuckCount, marryCount, killCount):
        self.charID = charID
        self.charName = charName
        self.nine = nine
        self.ten = ten
        self.eleven = eleven
        self.twelve = twelve
        self.thirteen = thirteen
        self.TW = TW
        self.SJA = SJA
        self.imagePath = imagePath
        self.fuckCount = fuckCount
        self.marryCount = marryCount
        self.killCount = killCount

    def increaseFuck(self):
        self.fuckCount += 1

    def increaseMarry(self):
        self.marryCount += 1

    def increaseKill(self):
        self.killCount += 1