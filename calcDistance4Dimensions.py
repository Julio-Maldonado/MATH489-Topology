points = [
    [1, 2, 3, 4],
    [3, 2, 1, 5],
    [-1, 3, 2, -4],
    [-3, 2, 1, -4],
    [-2, -1, -3, 4],
    [-4, 2, -3, 1],
    [0, -2, 3, -4],
    [0, 4, 3, 4],
    [2, 2, 4, 4],
    [-1, 5, 5, 8],
    [19, 0, 0, 0],
    [0, -4, 1, 9],
    [-5, -9, -2, -20],
    [-30, 8, -9, -7],
    [-3, -8, 19, 4],
    [19, 5, 12, 90],
    [2, 3, 9, 6],
    [-90, 3, 20, 20],
    [43, 72, 12, 8],
    [2, 9, 9, 3]
]

unitPoints = []

for i in range(len(points)):
    point = points[i].copy()
    point = list(map(lambda x: x * x, point))
    s = sum(point) ** 0.5
    # print(s)
    unitPoints.append(list(map(lambda x: x/s, points[i])))

for i in range(len(unitPoints)):
    point = list(map(lambda x: x * x, unitPoints[i]))
    s = sum(point)
    # print(s)

distFile = open("distanceMatrix.txt", "w+")
print(len(unitPoints))

for i in range(len(unitPoints)):
    print(i)
    p1 = unitPoints[i]
    for j in range(len(unitPoints)):
        p2 = unitPoints[j]
        dist = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2 + (p1[3] - p2[3]) ** 2
        dist = dist ** 0.5
        dist = str(dist)
        if j < i:
            distFile.write(dist[:5] + ",")
    
    distFile.write("\n")
