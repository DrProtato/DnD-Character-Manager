#spells section where new spells are added and can be searched

#spells will just have their name for now
#will get a text file with the spell list
spellsList = ["fireball", "avalanche", "magic missile", "skeleton wall", "firebolt", "fire of death", "blackhole", "hellfire"]
printedResults = []

#sorting the list
def sortList(spellList = []):
    i = 0
    while i < len(spellList):
        tempVar1 = spellList[i]
        if i + 1 == len(spellList):
            spellList.append(tempVar1)
        else:
            tempVar2 = spellList[i+1]
            if tempVar1 < tempVar2:

    return spellList



#adds spell using insertion sort
def addSpell(newSpell, spellList = []):
    i = 0
    while i < len(spellList):
        if newSpell < spellList[i]:
            tempVar = spellList[i]
            spellList[i] = newSpell
            newSpell = tempVar
        i = i + 1
    spellList.append(newSpell)
    return spellList

#searches for searched spell
def getSpell(searchSpell, spellList = [], resultsList = []):
    for i in spellList:
        if searchSpell in i:
            resultsList.append(i)
    resultsList = sortList(resultsList)
    return resultsList

response = input("Do you want to add a spell?\n")

if response == "y":
    newSpell = input("Spell Name? \n")
    spellsList = addSpell(newSpell, spellsList)


findSpell = input("Search for a spell\n")
results = getSpell(findSpell, spellsList, printedResults)
print(results)

