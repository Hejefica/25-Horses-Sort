import random
import numpy as np
import matplotlib.pyplot as plt

class Horse:
    def __init__(self, T, N = None, UP = None, LP = None):
        self.Time = T
        self.Name = N
        self.UpperPosition = UP
        self.LowerPosition = LP

#Competitors Registry
Competitors = np.zeros((5,5))
Shape = Competitors.shape
for x in range(Shape[0]):
    for y in range (Shape[1]):
        Competitors[x,y] = f'{random.random():.4f}'
print("25 horses into 5 groups:")
for x in range(5):
  print(Competitors[x]) 

#Race 1,2,3,4 & 5
print("Group sort from slower to faster:")
for x in range(5):
  Competitors[x].sort() 
  print(Competitors[x]) 
  

#Race 6
gSort = [Competitors[0,4], Competitors[1,4], Competitors[2,4], Competitors[3,4], Competitors[4,4]]
gSort.sort()
print("1st Place:", gSort[4])