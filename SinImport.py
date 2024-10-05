import random
likes = [[0] * 8 for n in range(8)]
for i in range(8):
	for j in range(8):
		likes[i][j] = random.randint(0, 1)
for i in range(8):
	print(likes[i])