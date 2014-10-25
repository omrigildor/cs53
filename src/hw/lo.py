from solver import solve
from vec import Vec
from mat import Mat
from GF2 import one

def D(n): return {(i,j) for i in range(n) for j in range(n)}

def button_vectors(n):
  return {(i,j):Vec(D(n),dict([((x,j),one) for x in range(max(i-1,0), min(i+2,n))]
                           +[((i,y),one) for y in range(max(j-1,0), min(j+2,n))]))
                           for (i,j) in D(n)}



b1 = Vec(D(19), {(7, 7):one, (6, 2):one, (3, 7):one,
      (2, 5):one, (8, 5):one, (7, 2):one, (1, 2):one,
     (6, 3):one, (5, 0):one, (0, 4):one, (2, 2):one,
      (6, 4):one, (5, 4):one, (0, 0):one, (1, 4):one,
      (8, 7):one, (0, 8):one, (6, 5):one, (2, 7):one,
      (8, 3):one, (7, 0):one, (4, 6):one, (6, 8):one,
      (7, 4):one, (0, 6):one, (1, 8):one, (7, 8):one, (2, 4):one})

print(solve(button_vectors(b1)))

b2=Vec(D(9), {(3,4):one})