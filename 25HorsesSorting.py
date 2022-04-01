from sqlite3 import Time


import matplotlib.pyplot as plt

class Horse:
    def __init__(self, N, T, UP, LP):
        self.Name = N
        self.Time = T
        self.UpperPosition = UP
        self.LowerPosition = LP

