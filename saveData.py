import pandas as pd

def saveToFile(characterList):
    charID = []
    charName = []
    nine = []
    ten = []
    eleven = []
    twelve = []
    thirteen = []
    TW = []
    SJA = []
    imagePath = []
    fuckCount = []
    marryCount = []
    killCount = []
    
    for character in characterList:
        charID.append(character.charID)
        charName.append(character.charName)
        nine.append(character.nine)
        ten.append(character.ten)
        eleven.append(character.eleven)
        twelve.append(character.twelve)
        thirteen.append(character.thirteen)
        TW.append(character.TW)
        SJA.append(character.SJA)
        imagePath.append(character.imagePath)
        fuckCount.append(character.fuckCount)
        marryCount.append(character.marryCount)
        killCount.append(character.killCount)

    data = {
        "charID": charID, "charName": charName, "nine": nine, "ten": ten, "eleven": eleven, "twelve": twelve, "thirteen": thirteen, "TW": TW, "SJA": SJA, "imagePath": imagePath, "fuckCount": fuckCount, "marryCount": marryCount, "killCount": killCount}

    df = pd.DataFrame(data)
    df.to_csv('savefile.csv')