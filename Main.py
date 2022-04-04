import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from math import sqrt
from HorseTree import HorseTree
from Tuple import Tuple

#Competitors Registry
Competitors = np.zeros((5, 5))
Shape = Competitors.shape
for x in range(Shape[0]):
    for y in range (Shape[1]):
        Competitors[x, y] = random.randint(0,1000)
print("25 horses into 5 groups:")
for x in range(5):
  print("Group ", x + 1, ":", Competitors[x])
print("")

#Race 1,2,3,4 & 5
print("Group sort from slower to faster:")
for x in range(5):
  Competitors[x].sort() 
  print("Race ", x + 1, ":", Competitors[x]) 
print("")
  
#Race 6
print("Group sort through fastest horses:")
print("                   |Race 6|")
R6 = Competitors[np.argsort(Competitors[:, -1])]
for x in range(5):
  print(R6[x]) 
print("")  
print("First place horse: ", int(R6[4,4]), "pts\n")

#Race 7
R7 = [R6[2, 4], R6[3, 4], R6[3, 3], R6[4, 3], R6[4, 2]]
R7.sort()
print("Race 7:", R7, "\n")
print ("Second place horse: ", int(R7[4]), "pts")
print ("Third place horse: ", int(R7[3]), "pts\n")

ConcatenatedArray = np.concatenate(R6)
ConcatenatedArray.sort()
print(ConcatenatedArray)

HorseTree = HorseTree(int(R6[0, 0]), "Horse 1")
HorseTree.Add(int(R6[0, 1]), "Horse 2")
HorseTree.Add(int(R6[0, 2]), "Horse 3")
HorseTree.Add(int(R6[0, 3]), "Horse 4")
HorseTree.Add(int(R6[0, 4]), "Horse 5")
HorseTree.Add(int(R6[1, 0]), "Horse 6")
HorseTree.Add(int(R6[1, 1]), "Horse 7")
HorseTree.Add(int(R6[1, 2]), "Horse 8")
HorseTree.Add(int(R6[1, 3]), "Horse 9")
HorseTree.Add(int(R6[1, 4]), "Horse 10")
HorseTree.Add(int(R6[2, 0]), "Horse 11")
HorseTree.Add(int(R6[2, 1]), "Horse 12")
HorseTree.Add(int(R6[2, 2]), "Horse 13")
HorseTree.Add(int(R6[2, 3]), "Horse 14")
HorseTree.Add(int(R6[2, 4]), "Horse 15")
HorseTree.Add(int(R6[3, 0]), "Horse 16")
HorseTree.Add(int(R6[3, 1]), "Horse 17")
HorseTree.Add(int(R6[3, 2]), "Horse 18")
HorseTree.Add(int(R6[3, 3]), "Horse 19")
HorseTree.Add(int(R6[3, 4]), "Horse 20")
HorseTree.Add(int(R6[4, 0]), "Horse 21")
HorseTree.Add(int(R6[4, 1]), "Horse 22")
HorseTree.Add(int(R6[4, 2]), "Horse 23")
HorseTree.Add(int(R6[4, 3]), "Horse 24")
HorseTree.Add(int(R6[4, 4]), "Horse 25")

"""x = 2
for x in range(Shape[0]):
    for y in range (Shape[1]):
        if R6[x, y] != R6[0, 0]:
            Tree.Add(int(R6[x, y],) "Horse " + string(x))
            x += 1"""

HorseTree.OrderedPrint()

Horses = ["" for x in range(25)]

for x in range(24):
  Data = HorseTree.Search(ConcatenatedArray[x]) 
  Horses[x] = Data.Name
  print(Horses[x])

def CalcDis(Dup1, Dup2):
    return sqrt(pow((Dup1.x - Dup2.x), 2) + pow((Dup1.y - Dup2.y), 2))

G = nx.Graph()
vertices_G = [Horses[24], Horses[23], Horses[22], Horses[21], Horses[20],Horses[19], Horses[18], 
              Horses[17], Horses[16], Horses[15], Horses[14], Horses[13], Horses[12], Horses[11], 
              Horses[10], Horses[9], Horses[8], Horses[7], Horses[6], Horses[5],Horses[4],
              Horses[3], Horses[2], Horses[1], Horses[0]]

G.add_nodes_from(vertices_G)

aristas_G = [(Horses[24], Horses[23]), (Horses[23], Horses[22]), (Horses[22], Horses[21]), (Horses[21], Horses[20]),
             (Horses[20], Horses[19]), (Horses[19], Horses[18]), (Horses[18], Horses[17]), (Horses[17], Horses[16]),
             (Horses[16], Horses[15]), (Horses[15], Horses[14]), (Horses[14], Horses[13]), (Horses[13], Horses[12]),
             (Horses[12], Horses[11]), (Horses[11], Horses[10]), (Horses[10], Horses[9]), (Horses[9], Horses[8]), 
             (Horses[8], Horses[7]), (Horses[7], Horses[6]), (Horses[6], Horses[5]), (Horses[5], Horses[4]),
             (Horses[4], Horses[3]), (Horses[3], Horses[2]), (Horses[2], Horses[1]), (Horses[1], Horses[0])]

G.add_edges_from(aristas_G)

ubica = {Horses[24]: (1, 21), Horses[23]: (3, 21), Horses[22]: (5, 21), Horses[21]: (7, 21), Horses[20]: (9, 21),
         Horses[19]: (11, 21), Horses[18]: (11, 19), Horses[17]: (11, 17), Horses[16]: (11, 15), Horses[15]: (11, 13), 
         Horses[14]: (11, 11), Horses[13]: (11, 9), Horses[12]: (11, 7), Horses[11]: (11, 5), Horses[10]: (11, 3),
         Horses[9]: (11, 1), Horses[8]: (13, 1), Horses[7]: (15, 1), Horses[6]: (17, 1), Horses[5]: (19, 1),
         Horses[4]: (21, 1), Horses[3]: (21, 3), Horses[2]: (21, 5), Horses[1]: (21, 7), Horses[0]: (21, 9)}

puntoA = Tuple()
puntoA.x = ubica[Horses[24]][0]
puntoA.y = ubica[Horses[24]][1]
puntoB = Tuple()
puntoB.x = ubica[Horses[23]][0]
puntoB.y = ubica[Horses[23]][1]
puntoC = Tuple()
puntoC.x = ubica[Horses[22]][0]
puntoC.y = ubica[Horses[22]][1]
puntoD = Tuple()
puntoD.x = ubica[Horses[21]][0]
puntoD.y = ubica[Horses[21]][1]
puntoE = Tuple()
puntoE.x = ubica[Horses[20]][0]
puntoE.y = ubica[Horses[20]][1]
puntoF = Tuple()
puntoF.x = ubica[Horses[19]][0]
puntoF.y = ubica[Horses[19]][1]
puntoG = Tuple()
puntoG.x = ubica[Horses[18]][0]
puntoG.y = ubica[Horses[18]][1]
puntoH = Tuple()
puntoH.x = ubica[Horses[17]][0]
puntoH.y = ubica[Horses[17]][1]
puntoI = Tuple()
puntoI.x = ubica[Horses[16]][0]
puntoI.y = ubica[Horses[16]][1]
puntoJ = Tuple()
puntoJ.x = ubica[Horses[15]][0]
puntoJ.y = ubica[Horses[15]][1]
puntoK = Tuple()
puntoK.x = ubica[Horses[14]][0]
puntoK.y = ubica[Horses[14]][1]
puntoL = Tuple()
puntoL.x = ubica[Horses[13]][0]
puntoL.y = ubica[Horses[13]][1]
puntoM = Tuple()
puntoM.x = ubica[Horses[12]][0]
puntoM.y = ubica[Horses[12]][1]
puntoN = Tuple()
puntoN.x = ubica[Horses[11]][0]
puntoN.y = ubica[Horses[11]][1]
puntoO = Tuple()
puntoO.x = ubica[Horses[10]][0]
puntoO.y = ubica[Horses[10]][1]
puntoP = Tuple()
puntoP.x = ubica[Horses[9]][0]
puntoP.y = ubica[Horses[9]][1]
puntoQ = Tuple()
puntoQ.x = ubica[Horses[8]][0]
puntoQ.y = ubica[Horses[8]][1]
puntoR = Tuple()
puntoR.x = ubica[Horses[7]][0]
puntoR.y = ubica[Horses[7]][1]
puntoS = Tuple()
puntoS.x = ubica[Horses[6]][0]
puntoS.y = ubica[Horses[6]][1]
puntoT = Tuple()
puntoT.x = ubica[Horses[5]][0]
puntoT.y = ubica[Horses[5]][1]
puntoU = Tuple()
puntoU.x = ubica[Horses[4]][0]
puntoU.y = ubica[Horses[4]][1]
puntoV = Tuple()
puntoV.x = ubica[Horses[3]][0]
puntoV.y = ubica[Horses[3]][1]
puntoY = Tuple()
puntoY.x = ubica[Horses[2]][0]
puntoY.y = ubica[Horses[2]][1]
puntoX = Tuple()
puntoX.x = ubica[Horses[1]][0]
puntoX.y = ubica[Horses[1]][1]
puntoZ = Tuple()
puntoZ.x = ubica[Horses[0]][0]
puntoZ.y = ubica[Horses[0]][1]

Puntos = {Horses[24]: puntoA, Horses[23]: puntoB, Horses[22]: puntoC, Horses[21]: puntoD, Horses[20]: puntoE, 
          Horses[19]: puntoF, Horses[18]: puntoG, Horses[17]: puntoH, Horses[16]: puntoI, Horses[15]: puntoJ, 
          Horses[14]: puntoK, Horses[13]: puntoL, Horses[12]: puntoM, Horses[11]: puntoN, Horses[10]: puntoO, 
          Horses[9]: puntoP, Horses[8]: puntoQ, Horses[7]: puntoR, Horses[6]: puntoS, Horses[5]: puntoT, 
          Horses[4]: puntoU, Horses[3]: puntoV, Horses[2]: puntoY, Horses[1]: puntoX, Horses[0]: puntoZ}
          
cont: int = 0
for i in aristas_G:
    Pa = Puntos[aristas_G[cont][0]]
    Pb = Puntos[aristas_G[cont][1]]
    G.edges[i]['distancia'] = CalcDis(Pa, Pb)*100
    print('La distancia entre ', aristas_G[cont], G.edges[i],'[METROS]')
    cont = cont + 1
nx.draw(G, pos=ubica, node_color='gray', with_labels=True)

plt.show()