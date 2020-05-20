import random
j = 0
i = 0
statlist = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
while i < 6:
	dice = [a,b,c,d]
	dice[a] = random.randint(1,6)
	dice[b] = random.randint(1,6)
	dice[c] = random.randint(1,6)
	dice[d] = random.randint(1,6)
	dice.sort()
	stat = dice[1] + dice[2] + dice[3]
	print(statlist[i] + ": " + str(stat))
	j = j + stat
	i = i + 1
print("Stat Total: " + str(j))
