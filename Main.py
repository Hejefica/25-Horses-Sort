import random
import string
import numpy as np
import matplotlib.pyplot as plt
from Tree import Tree

#Competitors Registry
Competitors = np.zeros((5,5))
Shape = Competitors.shape
for x in range(Shape[0]):
    for y in range (Shape[1]):
        Competitors[x,y] = f'{random.random():.4f}'
print("25 horses into 5 groups:")
for x in range(5):
  print("Group ", x+1, ":", Competitors[x])
print("")

#Race 1,2,3,4 & 5
print("Group sort from slower to faster:")
for x in range(5):
  Competitors[x].sort() 
  print("Race ", x+1, ":", Competitors[x]) 
print("")
  
#Race 6
print("Group sort through fastest horses:")
print("                            |Race 6|")
R6 = Competitors[np.argsort(Competitors[:,-1])]
for x in range(5):
  print(R6[x]) 
print("First place horse: ", R6[4,4])



#Race 7
R7 = [R6[2,4], R6[3,4], R6[3,3], R6[4,3], R6[4,2]]
R7.sort()
print("Race 7:", R7)
print ("Second place horse: ", R7[4])
print ("Third place horse: ", R7[3])

Tree = Tree(R6[0,0], "Horse 1")
"""Tree.Add(R6[0,1], "Horse 2")
Tree.Add(R6[0,2], "Horse 3")
Tree.Add(R6[0,3], "Horse 4")
Tree.Add(R6[0,4], "Horse 5")
Tree.Add(R6[1,0], "Horse 6")
Tree.Add(R6[1,1], "Horse 7")
Tree.Add(R6[1,2], "Horse 8")
Tree.Add(R6[1,3], "Horse 9")
Tree.Add(R6[1,4], "Horse 10")
Tree.Add(R6[2,0], "Horse 11")
Tree.Add(R6[2,1], "Horse 12")
Tree.Add(R6[2,2], "Horse 13")
Tree.Add(R6[2,3], "Horse 14")
Tree.Add(R6[2,4], "Horse 15")
Tree.Add(R6[3,0], "Horse 16")
Tree.Add(R6[3,1], "Horse 17")
Tree.Add(R6[3,2], "Horse 18")
Tree.Add(R6[3,3], "Horse 19")
Tree.Add(R6[3,4], "Horse 20")
Tree.Add(R6[4,0], "Horse 21")
Tree.Add(R6[4,1], "Horse 22")
Tree.Add(R6[4,2], "Horse 23")
Tree.Add(R6[4,3], "Horse 24")
Tree.Add(R6[4,4], "Horse 25")"""

x = 2
for x in range(Shape[0]):
    for y in range (Shape[1]):
        if R6[x,y] != R6[0,0]:
            Tree.Add(R6[x,y], "Horse " + string(x))
            x += 1

Tree.OrderedPrint()