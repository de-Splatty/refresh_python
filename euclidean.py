import math

def euclidean_distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

p1 = (2, 3)
p2 = (10, 8)
print(euclidean_distance(p1, p2))