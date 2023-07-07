from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QPixmap, QIcon, QFont
from PyQt5.QtCore import *
import sys
import random
import pandas as pd

from character import Character
from saveData import saveToFile

##  WINDOW PARAMETERS
xpos = 20
ypos = 60
width = 1200
height = 800

## CHARACTER LIST
characterList = []
character1 = "placeholder"
character2 = "placeholder"
character3 = "placeholder"
nineEra = True
tenEra = True
elevenEra = True
twelveEra = True
thirteenEra = True
Torchwood = True
SarahJaneAdventures = True
ListUpdated = False



class FMKDoctorWho(QMainWindow):
    def __init__(self):
        super(FMKDoctorWho, self).__init__()
        self.setGeometry(xpos, ypos, width, height)
        self.setWindowTitle('DW Fuck Marry Kill')
        self.initUI()
        self.createCharacterList()
        self.selectCharacters()
    

    def createCharacterList(self):
        global characterList
        characterList = []
        fullCharacterList = []
        df = pd.read_csv('characters.csv')
        numRows = len(df.index)
        rowNumber = 0

        while rowNumber < numRows:
            row = df.loc[rowNumber]
            fullCharacterList.append(Character(row.charID, row.charName, row.nine, row.ten, row.eleven, row.twelve, row.thirteen, row.TW, row.SJA, row.imagePath, row.fuckCount, row.marryCount, row.killCount))
            rowNumber += 1
        
        for character in fullCharacterList:
            if character.nine == True and nineEra == True:
                characterList.append(character)
            if character.ten == True and tenEra == True and character not in characterList:
                characterList.append(character)
            if character.eleven == True and elevenEra == True and character not in characterList:
                characterList.append(character)
            if character.twelve == True and twelveEra == True and character not in characterList:
                characterList.append(character)
            if character.thirteen == True and thirteenEra == True and character not in characterList:
                characterList.append(character)
            if character.TW == True and Torchwood == True and character not in characterList:
                characterList.append(character)
            if character.SJA == True and SarahJaneAdventures == True and character not in characterList:
                characterList.append(character)
        

    def selectCharacters(self):
        global character1
        global character2
        global character3
        global ListUpdated

        if ListUpdated == True:
            self.createCharacterList()
            ListUpdated = False

        index1 = random.randint(0, len(characterList) - 1)
        index2 = random.randint(0, len(characterList) - 1)
        while index2 == index1:
            index2 = random.randint(0, len(characterList) - 1)
        index3 = random.randint(0, len(characterList) - 1)
        while index3 == index1 or index3 == index2:
            index3 = random.randint(0, len(characterList) - 1)
        
        character1 = characterList[index1]
        character2 = characterList[index2]
        character3 = characterList[index3]
        self.setupPage(character1, character2, character3)

    def initUI(self):
         ## Character 1
        self.characterName1 = QtWidgets.QLabel(self)
        self.characterName1.setFont(QFont("Arial", 18))
        self.characterName1.setText("placeholder1")
        self.characterName1.move(100, 65)
        self.characterName1.adjustSize()
        self.characterImage1 = QLabel(self)
        pixmap1 = QPixmap('images_resized\TARDIS.jpg')
        self.characterImage1.setPixmap(pixmap1)
        self.characterImage1.move(100, 100)
        self.characterImage1.adjustSize()
        ## Character 2
        self.characterName2 = QtWidgets.QLabel(self)
        self.characterName2.setFont(QFont("Arial", 18))
        self.characterName2.setText('placeholder2')
        self.characterName2.move(500, 65)
        self.characterName2.adjustSize()
        self.characterImage2 = QLabel(self)
        pixmap2 = QPixmap('images_resized\TARDIS.jpg')
        self.characterImage2.setPixmap(pixmap2)
        self.characterImage2.move(500, 100)
        self.characterImage2.adjustSize()
        ## Character 3
        self.characterName3 = QtWidgets.QLabel(self)
        self.characterName3.setFont(QFont("Arial", 18))
        self.characterName3.setText('placeholder3')
        self.characterName3.move(900, 65)
        self.characterName3.adjustSize()
        self.characterImage3 = QLabel(self)
        pixmap3 = QPixmap('images_resized\TARDIS.jpg')
        self.characterImage3.setPixmap(pixmap3)
        self.characterImage3.move(900, 100)
        self.characterImage3.adjustSize()

        ## Check Boxes
        self.fuck1 = QtWidgets.QCheckBox(self)
        self.fuck1.setFont(QFont('Arial', 16))
        self.fuck1.setText("Fuck")
        self.fuck1.move(150, 450)
        self.fuck2 = QtWidgets.QCheckBox(self)
        self.fuck2.setFont(QFont('Arial', 16))
        self.fuck2.setText("Fuck")
        self.fuck2.move(550, 450)
        self.fuck3 = QtWidgets.QCheckBox(self)
        self.fuck3.setFont(QFont('Arial', 16))
        self.fuck3.setText("Fuck")
        self.fuck3.move(950, 450)
       
        self.marry1 = QtWidgets.QCheckBox(self)
        self.marry1.setFont(QFont('Arial', 16))
        self.marry1.setText("Marry")
        self.marry1.move(150, 525)
        self.marry2 = QtWidgets.QCheckBox(self)
        self.marry2.setFont(QFont('Arial', 16))
        self.marry2.setText("Marry")
        self.marry2.move(550, 525)
        self.marry3 = QtWidgets.QCheckBox(self)
        self.marry3.setFont(QFont('Arial', 16))
        self.marry3.setText("Marry")
        self.marry3.move(950, 525)

        self.kill1 = QtWidgets.QCheckBox(self)
        self.kill1.setFont(QFont('Arial', 16))
        self.kill1.setText("Kill")
        self.kill1.move(150, 600)
        self.kill2 = QtWidgets.QCheckBox(self)
        self.kill2.setFont(QFont('Arial', 16))
        self.kill2.setText("Kill")
        self.kill2.move(550, 600)
        self.kill3 = QtWidgets.QCheckBox(self)
        self.kill3.setFont(QFont('Arial', 16))
        self.kill3.setText("Kill")
        self.kill3.move(950, 600)

        self.btnCustomizeCharacters = QtWidgets.QPushButton(self)
        self.btnCustomizeCharacters.setText("Character Settings")
        self.btnCustomizeCharacters.adjustSize()
        self.btnCustomizeCharacters.move(1000, 25)

        self.btnStatistics = QtWidgets.QPushButton(self)
        self.btnStatistics.setText("Statistics")
        self.btnStatistics.adjustSize()
        self.btnStatistics.move(75, 25)


        self.update()
        self.fuck1.stateChanged.connect(self.uncheck)
        self.fuck2.stateChanged.connect(self.uncheck)
        self.fuck3.stateChanged.connect(self.uncheck)
        self.marry1.stateChanged.connect(self.uncheck)
        self.marry2.stateChanged.connect(self.uncheck)
        self.marry3.stateChanged.connect(self.uncheck)
        self.kill1.stateChanged.connect(self.uncheck)
        self.kill2.stateChanged.connect(self.uncheck)
        self.kill3.stateChanged.connect(self.uncheck)
        self.btnCustomizeCharacters.clicked.connect(self.setCharacterList)
        self.btnStatistics.clicked.connect(self.openStatistics)
    
    def setupPage(self, character1, character2, character3):
        ## Character 1
        print(character1.charName)
        print(character1.imagePath)
        self.characterName1.setFont(QFont("Arial", 18))
        self.characterName1.setText(character1.charName)
        self.characterName1.move(100, 65)
        self.characterName1.adjustSize()
        pixmap1 = QPixmap(character1.imagePath)
        self.characterImage1.setPixmap(pixmap1)
        self.characterImage1.move(100, 100)
        self.characterImage1.adjustSize()
        ## Character 2
        self.characterName2.setFont(QFont("Arial", 18))
        self.characterName2.setText(character2.charName)
        self.characterName2.move(500, 65)
        self.characterName2.adjustSize()
        pixmap2 = QPixmap(character2.imagePath)
        self.characterImage2.setPixmap(pixmap2)
        self.characterImage2.move(500, 100)
        self.characterImage2.adjustSize()
        ## Character 3
        self.characterName3.setFont(QFont("Arial", 18))
        self.characterName3.setText(character3.charName)
        self.characterName3.move(900, 65)
        self.characterName3.adjustSize()
        pixmap3 = QPixmap(character3.imagePath)
        self.characterImage3.setPixmap(pixmap3)
        self.characterImage3.move(900, 100)
        self.characterImage3.adjustSize()

        self.btnNext = QtWidgets.QPushButton(self)
        self.btnNext.setText("NEXT >>")
        self.btnNext.setFont(QFont('Arial', 18))
        self.btnNext.adjustSize()
        self.btnNext.move(550, 700)

        self.btnNext.clicked.connect(self.checkForCompletion)

    def checkForCompletion(self):
        if self.fuck1.isChecked() or self.fuck2.isChecked() or self.fuck3.isChecked():
            print("fuck")
            if self.marry1.isChecked() or self.marry2.isChecked() or self.marry3.isChecked():
                print("marry")
                if self.kill1.isChecked() or self.kill2.isChecked() or self.kill3.isChecked():
                    print("kill")
                    self.saveAnswers()
                else:
                    print('no')
            else:
                print('no')
        else:
            print('no')
           

    def uncheck(self, state):
        if state == Qt.Checked:
            if self.sender() == self.fuck1:
                self.fuck2.setChecked(False)
                self.fuck3.setChecked(False)
                self.marry1.setChecked(False)
                self.kill1.setChecked(False)
            if self.sender() == self.fuck2:
                self.fuck1.setChecked(False)
                self.fuck3.setChecked(False)
                self.marry2.setChecked(False)
                self.kill2.setChecked(False)
            if self.sender() == self.fuck3:
                self.fuck1.setChecked(False)
                self.fuck2.setChecked(False)
                self.marry3.setChecked(False)
                self.kill3.setChecked(False)

            if self.sender() == self.marry1:
                self.marry2.setChecked(False)
                self.marry3.setChecked(False)
                self.fuck1.setChecked(False)
                self.kill1.setChecked(False)
            if self.sender() == self.marry2:
                self.marry1.setChecked(False)
                self.marry3.setChecked(False)
                self.fuck2.setChecked(False)
                self.kill2.setChecked(False)
            if self.sender() == self.marry3:
                self.marry1.setChecked(False)
                self.marry2.setChecked(False)
                self.fuck3.setChecked(False)
                self.kill3.setChecked(False)

            if self.sender() == self.kill1:
                self.kill2.setChecked(False)
                self.kill3.setChecked(False)
                self.fuck1.setChecked(False)
                self.marry1.setChecked(False)
            if self.sender() == self.kill2:
                self.kill1.setChecked(False)
                self.kill3.setChecked(False)
                self.fuck2.setChecked(False)
                self.marry2.setChecked(False)
            if self.sender() == self.kill3:
                self.kill1.setChecked(False)
                self.kill2.setChecked(False)
                self.fuck3.setChecked(False)
                self.marry3.setChecked(False)

    def saveAnswers(self):
        if self.fuck1.isChecked():
            character1.increaseFuck()
        elif self.fuck2.isChecked():
            character2.increaseFuck()
        elif self.fuck3.isChecked():
            character3.increaseFuck()
        if self.marry1.isChecked():
            character1.increaseMarry()
        elif self.marry2.isChecked():
            character2.increaseMarry()
        elif self.marry3.isChecked():
            character3.increaseMarry()
        if self.kill1.isChecked():
            character1.increaseKill()
        elif self.kill2.isChecked():
            character2.increaseKill()
        elif self.kill3.isChecked():
            character3.increaseKill()

        saveToFile(characterList)

        self.fuck1.setChecked(False)
        self.fuck2.setChecked(False)
        self.fuck3.setChecked(False)
        self.marry1.setChecked(False)
        self.marry2.setChecked(False)
        self.marry3.setChecked(False)
        self.kill1.setChecked(False)
        self.kill2.setChecked(False)
        self.kill3.setChecked(False)
        self.selectCharacters()

    def setCharacterList(self):
        self.pop = CharacterSettings()
        self.pop.show()

    def openStatistics(self):
        self.pop = Statistics()
        self.pop.show()

class CharacterSettings(QWidget):
    def __init__(self):
        super(CharacterSettings, self).__init__()
        self.setGeometry(100, 100, 300, 450)
        self.setWindowTitle('Character Settings')
        self.CS_initUI()

    def CS_initUI(self):
        self.ninth = QtWidgets.QCheckBox(self)
        self.ninth.setText('Ninth Doctor Era')
        self.ninth.move(50, 50)
        if nineEra == True:
            self.ninth.setChecked(True)
        self.tenth = QtWidgets.QCheckBox(self)
        self.tenth.setText('Tenth Doctor Era')
        self.tenth.move(50, 100)
        if tenEra == True:
            self.tenth.setChecked(True)
        self.eleventh = QtWidgets.QCheckBox(self)
        self.eleventh.setText('Eleventh Doctor Era')
        self.eleventh.move(50, 150)
        if elevenEra == True:
            self.eleventh.setChecked(True)
        self.twelfth = QtWidgets.QCheckBox(self)
        self.twelfth.setText('Twelfth Doctor Era')
        self.twelfth.move(50, 200)
        if twelveEra == True:
            self.twelfth.setChecked(True)
        self.thirteenth = QtWidgets.QCheckBox(self)
        self.thirteenth.setText('Thirteenth Doctor Era')
        self.thirteenth.move(50, 250)
        if thirteenEra == True:
            self.thirteenth.setChecked(True)
        self.TW = QtWidgets.QCheckBox(self)
        self.TW.setText('Torchwood')
        self.TW.move(50, 300)
        if Torchwood == True:
            self.TW.setChecked(True)
        self.SJA = QtWidgets.QCheckBox(self)
        self.SJA.setText('The Sarah Jane Adventures')
        self.SJA.move(50, 350)
        if SarahJaneAdventures == True:
            self.SJA.setChecked(True)
        self.btnSave = QtWidgets.QPushButton(self)
        self.btnSave.setText("SAVE")
        self.btnSave.move(50, 400)
        self.btnSave.clicked.connect(self.CS_save)

    def CS_save(self, state):
        global nineEra
        global tenEra
        global elevenEra
        global twelveEra
        global thirteenEra
        global Torchwood
        global SarahJaneAdventures
        global ListUpdated

        if self.ninth.isChecked():
            nineEra = True
        else:
            nineEra = False
        if self.tenth.isChecked():
            tenEra = True
        else:
            tenEra = False
        if self.eleventh.isChecked():
            elevenEra = True
        else:
            elevenEra = False
        if self.twelfth.isChecked():
            twelveEra = True
        else:
            twelveEra = False
        if self.thirteenth.isChecked():
            thirteenEra = True
        else:
            thirteenEra = False
        if self.TW.isChecked():
            Torchwood = True
        else:
            Torchwood = False
        if self.SJA.isChecked():
            SarahJaneAdventures = True
        else:
            SarahJaneAdventures = False

        ListUpdated = True
        self.close()

class Statistics(QWidget):
    def __init__(self):
        super(Statistics, self).__init__()
        self.setGeometry(50, 50, 800, 700)
        self.setWindowTitle('Statistics')
        self.S_initUI()

    def S_initUI(self):
        df = pd.read_csv('savefile.csv')
        df_fuckSort = df.sort_values('fuckCount', ascending=False).head(25)
        fuckDataName = df_fuckSort[["charName", "fuckCount"]]
        df_marrySort = df.sort_values('marryCount', ascending=False).head(25)
        marryDataName = df_marrySort[["charName", "marryCount"]]
        df_killSort = df.sort_values('killCount', ascending=False).head(25)
        killDataName = df_killSort[["charName", "killCount"]]
       
        self.fuckname1 = QtWidgets.QLabel(self)
        self.fuckname1.setText(fuckDataName.to_string())
        self.fuckname1.move(35, 80)
        self.marryname1 = QtWidgets.QLabel(self)
        self.marryname1.setText(marryDataName.to_string())
        self.marryname1.move(305, 80)
        self.killname1 = QtWidgets.QLabel(self)
        self.killname1.setText(killDataName.to_string())
        self.killname1.move(575, 80)

        self.fuckHead = QtWidgets.QLabel(self)
        self.fuckHead.setText("Most Fucked")
        self.fuckHead.move(60, 50)
        self.marryHead = QtWidgets.QLabel(self)
        self.marryHead.setText("Most Married")
        self.marryHead.move(330, 50)
        self.killHead = QtWidgets.QLabel(self)
        self.killHead.setText("Most Killed")
        self.killHead.move(600, 50)
        
        
        
        

def window():
    app = QApplication(sys.argv)
    win = FMKDoctorWho()

    win.show()
    

    sys.exit(app.exec_())



window()