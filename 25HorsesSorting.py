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
print("Group sort fastest of the fastest:")
R6 = Competitors[np.argsort(Competitors[:,-1])]
for x in range(5):
  print(R6[x]) 
print("First place horse: ", R6[4,4])

#Race 7
R7 = [R6[2,4], R6[3,4], R6[3,3], R6[4,3], R6[4,2]]
R7.sort()
print ("Second place horse: ", R7[4])
print ("Third place horse: ", R7[3])