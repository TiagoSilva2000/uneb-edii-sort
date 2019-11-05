import sys
sys.path.insert(1, '/home/ttiago/codes/ed2/trab1')
from typing import List
import copy
import time
from classes.Virus import Virus

def selectionAccessGT (virusList:List[Virus])-> None:
  minIndex:int = 0
  for i in range(len(virusList) - 1):
    minIndex = i
    for j in range (i+1, len(virusList)):
      if (virusList[j].getAccess() < virusList[minIndex].getAccess()):
        minIndex = j
    virusList[minIndex], virusList[i] = virusList[i], virusList[minIndex]

def selectionAccessLT (virusList:List[Virus])-> None:
  maxIndex:int = 0
  for i in range(len(virusList) - 1):
    maxIndex = i
    for j in range (i+1, len(virusList)):
      if (virusList[j].getAccess() > virusList[maxIndex].getAccess()):
        maxIndex = j
    virusList[maxIndex], virusList[i] = virusList[i], virusList[maxIndex]

def selectionDateLT(virusList:List)->None:
  minIndex:int = 0
  for i in range(len(virusList) - 1):
    minIndex = i
    for j in range(i+1, len(virusList)):
      if (virusList[j].getDate() < virusList[minIndex].getDate()):
        minIndex = j
    virusList[i], virusList[minIndex] = virusList[minIndex], virusList[i]
