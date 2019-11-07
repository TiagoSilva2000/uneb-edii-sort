import sys
sys.path.insert(1, '/home/ttiago/codes/ed2/trab1')

# from main import dateLT, accessGT, accessLT
import random
from typing import List
from classes.Virus import Virus
import copy

def accessLT(arr:List[Virus], a:int, comp:Virus)-> bool:
  return arr[a].getAccess() < comp.getAccess()

def accessGT(arr:List[Virus], a:int, comp:Virus)-> bool:
  return arr[a].getAccess() > comp.getAccess()

def dateLT(arr:List[Virus], a:int, comp:Virus)-> bool:
  return arr[a].getDate() < comp.getDate()

def quickSort(listy, initialPosition, finalPosition, cmpFunction)-> None:
    if initialPosition < finalPosition:
        pivotIdx:int = partition(listy, initialPosition, finalPosition, cmpFunction)
        quickSort(listy, initialPosition, (pivotIdx-1), cmpFunction)
        quickSort(listy, (pivotIdx + 1), finalPosition, cmpFunction)

def partition(listy, initialPosition, finalPosition, cmpFunction)-> int:
    pivotValue:Virus = copy.copy(listy[finalPosition])
    leftIdx:int = initialPosition - 1; rightIdx:int = initialPosition

    while rightIdx < (finalPosition - 1):
      if cmpFunction(listy, rightIdx, pivotValue):
        leftIdx += 1
        listy[leftIdx], listy[rightIdx] = listy[rightIdx], listy[leftIdx]
      rightIdx += 1

    leftIdx += 1
    listy[leftIdx], listy[finalPosition] = listy[finalPosition], listy[leftIdx]

    return leftIdx

def quickDateLT(listy):
  quickSort(listy, 0, len(listy)-1, dateLT)

def quickAccessLT(listy):
  quickSort(listy, 0, len(listy)-1, accessLT)

def quickAccessGT(listy):
  quickSort(listy, 0, len(listy)-1, accessGT)