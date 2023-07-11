level_one = []

# for x in range(100, 300, 45):
#     for y in range(200, 300, 25):
#         level_one.append((x, y))
for x in range(-350, 350, 45):
    for y in range(100, 250, 25):
        level_one.append((x, y))

level_two = []
for x in range(-250, 250, 45):
    for y in range(0, 300, 25):
        if x not in range(-200, -100) and x not in range(100, 200):
            level_two.append((x, y))

level_three = []
for x in range(-300, 300, 45):
    for y in range(-100, 300, 25):
        if x not in range(-250, -200) and x not in range(200, 250) and x not in range(-50, 50) and y not in range(100, 150):
            level_three.append((x, y))