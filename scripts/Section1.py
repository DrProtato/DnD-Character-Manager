#character creation first section

#inplace for when the ui is added

import random



#temp solution until ui is created
def classSect(isRan):
    classList = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer",
                 "Warlock", "Wizard"]
    if isRan == True:
        dndClass = classList[random.randint(0, (len(classList) - 1))]
        return dndClass
    else:
        while True:
            try:
                print(classList)
                dndClass = classList[int(input("Which class do you want to be? (type a number from 1 to 12)\n")) - 1]
                return dndClass
            except:
                print("Try again.  Make sure you type a valid number")

