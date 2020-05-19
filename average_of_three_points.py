# Codigo para calcular a media aritmetica de 3 pontos com coordenas x,y

import math

def average_points(p1, p2, p3):
  sum = dist(p1,p2) + dist(p1,p3) + dist(p2,p3)
  avg = sum / 3
  return avg

def dist(p1, p2):
  (x1, y1), (x2, y2) = p1, p2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(average_points((1,2), (2,3), (5, 6)))