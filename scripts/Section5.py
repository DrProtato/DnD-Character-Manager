#spells section where new spells are added and can be searched

#spells will just have their name for now
#will get a text file with the spell list

#sorting the list
def sortList(goodCount, spellList = []):
    while True:
        i = 0
        if goodCount == len(spellList) - 1:
            break
        else:
            goodCount = 0
            while i < len(spellList):
                if i + 1 != len(spellList):
                    tempVar1 = spellList[i]
                    tempVar2 = spellList[i+1]
                    if tempVar1 > tempVar2:
                        spellList[i] = tempVar2
                        spellList[i+1] = tempVar1
                    else:
                        goodCount = goodCount + 1
                i = i +1
    return spellList

#adds spell using insertion sort
def addSpell(newSpell, goodCount):
    spellList = ["fireball", "avalanche", "magic missile", "skeleton wall", "firebolt", "fire of death", "blackhole",
                  "hellfire", "blackbody", "firewall", "flames of olympus"]
    i = 0
    while i < len(spellList):
        if newSpell < spellList[i]:
            tempVar = spellList[i]
            spellList[i] = newSpell
            newSpell = tempVar
        i = i + 1
    spellList.append(newSpell)
    spellList = sortList(goodCount, spellList)
    return spellList

#searches for searched spell
def getSpell(searchSpell, goodCount, resultsList = [], spellList = []):
    for i in spellList:
        if searchSpell in i:
            resultsList.append(i)
    if len(resultsList) > 0:
        resultsList = sortList(goodCount, resultsList)
        return resultsList
    else:
        noResults = "No results were found"
        return noResults


def start():
    spellsList = []
    printedResults = []
    goodCount = 0
    response = input("Do you want to add a spell? (yes/no)\n")

    if response == "yes":
        newSpell = input("Spell Name? \n")
        spellsList = addSpell(newSpell, goodCount)


    findSpell = input("Search for a spell\n")
    results = getSpell(findSpell, printedResults, spellsList)
    return results

