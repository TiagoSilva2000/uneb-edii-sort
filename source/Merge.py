import sys
sys.path.insert(1, '/home/ttiago/codes/ed2/trab1')
from typing import List
from classes.Virus import Virus
import copy

def mergeCmpAccessGT(arrA:List[Virus], arrB:List[Virus], idxA:int, idxB:int)-> bool:
  return arrA[idxA].getAccess() > arrB[idxB].getAccess()

def mergeCmpAccessLT(arrA:List[Virus], arrB:List[Virus], idxA:int, idxB:int)-> bool:
  return arrA[idxA].getAccess() < arrB[idxB].getAccess()

def mergeCmpDateLT(arrA:List[Virus], arrB:List[Virus], idxA:int, idxB:int)-> bool:
  return arrA[idxA].getDate() < arrB[idxB].getDate()

def realMerge (objList:List[Virus], cmpFunction, ini:int, middle:int, final:int):
  tempA:List[Virus] = []; tempB:List[Virus] = []
  leftI:int = 0; rightI:int = 0
  leftRange:int = middle-ini+1;rightRange:int = final - middle; arrIt:int = 0

  for i in range(leftRange):
    tempA.append(copy.copy(objList[ini + i]))
  for i in range(rightRange):
    tempB.append(copy.copy(objList[middle + 1 + i]))

  while leftI < leftRange and rightI < rightRange:
    if cmpFunction(tempA, tempB, leftI, rightI):
      objList[arrIt] = tempA[leftI]
      leftI += 1
    else:
      objList[arrIt] = tempB[rightI]
      rightI += 1
    arrIt += 1

  while leftI < leftRange:
    objList[arrIt] = tempA[leftI]
    arrIt += 1; leftI += 1
  while rightI < rightRange:
    objList[arrIt] = tempB[rightI]
    arrIt += 1; rightI += 1

def mergeSort (objList:List[Virus], cmpFunction, ini:int, final:int):
  if ini < final:
    middle:int = (ini + final) // 2
    mergeSort(objList, cmpFunction, ini, middle)
    mergeSort(objList, cmpFunction, middle+1, final)
    realMerge(objList, cmpFunction, ini, middle, final)


def mergeAccessGT(objList:List[Virus]):
  mergeSort(objList, mergeCmpAccessGT, 0, len(objList) - 1)

def mergeAccessLT(objList:List[Virus]):
  mergeSort(objList, mergeCmpAccessLT, 0, len(objList) - 1)

def mergeDateLT(objList:List[Virus]):
  mergeSort(objList, mergeCmpDateLT, 0, len(objList) - 1)
