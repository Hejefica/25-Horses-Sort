import random
import numpy as np
import matplotlib.pyplot as plt

class Horse:
    def __init__(self, T, N = None, UP = None, LP = None):
        self.Time = T
        self.Name = N
        self.UpperPosition = UP
        self.LowerPosition = LP

def Random():
    return f'{random.random():.4f}'

gA = [Random(),Random(),Random(),Random(),Random()]
gB = [Random(),Random(),Random(),Random(),Random()]
gC = [Random(),Random(),Random(),Random(),Random()]
gD = [Random(),Random(),Random(),Random(),Random()]
print("25 horses into 5 groups:", "\n", gA, "\n", gB, "\n", gC, "\n", gD)

#Race 1
gA.sort()
gB.sort()
gC.sort()
gD.sort()
print("Group sort from slower to faster:", "\n", gA, "\n", gB, "\n", gC, "\n", gD)
