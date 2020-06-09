import random

#stats are rolled at random
def statRoll():
	j = 0
	i = 0
	statlist = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
	statlistnum = []
	while i < 6:
		dice = []
		while len(dice) < 4:
			dice.append(random.randint(1,6))
		dice.sort()
		stat = dice[1] + dice[2] + dice[3]
		statlistnum.append(stat)
		print(str(statlist[i]) + ": " + str(statlistnum[i]))
		j = j + stat
		i = i + 1
	print("Stat Total: " + str(j))

#dnd's standard stat array
def standardArray():
	standSet = [15, 14, 13, 12, 10, 8]

#point buy system
def pointBuy():
	currentStats = [8,8,8,8,8,8,]
	currentPoints = 27

