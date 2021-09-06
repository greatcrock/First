"""
This is a mission to check the similarity of two triangles.

You are given two lists as coordinates of vertices of each triangle.
You have to return a bool. (The triangles are similar or not)

Input:

Two lists as coordinates of vertices of each triangle.
Coordinates is three tuples of two integers.
Output: True or False.

Precondition:
-10 ≤ x(, y) coordinate ≤ 10

similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True
similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False
similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True
"""
from typing import List, Tuple
import math
Coords = List[Tuple[int, int]]

def sider(coords):
    a,b,c = coords
    side1 = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    side2 = math.sqrt((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2)
    side3 = math.sqrt((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)
    return sorted([side1, side2, side3])

def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    a1, b1, c1 = sider(coords_1)
    a2, b2, c2 = sider(coords_2)

    return round(a1 / a2, 4) == round(b1 / b2, 4) == round(c1 / c2, 4)

print(similar_triangles([[-2,-5],[-3,-1],[3,0]],[[5,10],[8,-2],[-10,-5]]))
# print(sider([(0, 0), (1, 2), (2, 0)]))
# # assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
# # print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))
# # print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))
# print(similar_triangles([(0,0),(0,3),(2,0)], [(3,0),(5,3),(5,0)]))
# # assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
# # assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
# # assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
# # assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
# # assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
