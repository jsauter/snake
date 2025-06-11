background = [1, 1, 2, 2, 2, 1]
screen = [0]*len(background)
for i in range(len(background)):
    screen[i] = background[i]
print(screen)
playerpos = 3
screen[playerpos] = 8
print(screen)