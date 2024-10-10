l = [
    (1, 2),
    (-4, -5.5),
    (10, -10),
    (-2, 2)
]

print(sorted(l, key=lambda d : abs(d[0]-d[1]), reverse=True))
