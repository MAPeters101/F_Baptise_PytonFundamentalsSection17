data = {
    'S1': (100, 200, 80, 180),
    'S2': (10, 20, 8, 18),
    'S3': (50, 150, 50, 150)
}

def find_extreme(d, is_min=True):
    if is_min:
        return min(d, key=lambda key: d[key][1] - d[key][2])
    else:
        return max(d, key=lambda key: d[key][1] - d[key][2])

print(find_extreme(data))
print(find_extreme(data, is_min=False))

