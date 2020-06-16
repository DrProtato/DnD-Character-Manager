#spells section where new spells are added and can be searched

#spells will just have their name for now
spellsList = []
printedResults = []
#adds spell using insertion sort
def addSpell(spellList, newSpell):
    for i in spellList:
        if newSpell < i:
            tempVar = i


    return spellList

#searches for searched spell
def getSpell(searchSpell, spellList = [], resultsList = []):
    for i in spellList:
        if searchSpell in i:
            resultsList.append(i)
    return resultsList

response = input("Do you want to add a spell?")

newSpell = input("Spell Name? ")
