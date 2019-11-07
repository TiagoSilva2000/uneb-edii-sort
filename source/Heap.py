import sys
sys.path.insert(1, '/home/ttiago/codes/ed2/trab1')

from classes.Virus import Virus
from typing import List
# from main import accessGT, accessLT, dateLT

def accessLT(arr:List[Virus], a:int, b:int)-> bool:
  return arr[a].getAccess() < arr[b].getAccess()

def accessGT(arr:List[Virus], a:int, b:int)-> bool:
  return arr[a].getAccess() > arr[b].getAccess()

def dateLT(arr:List[Virus], a:int, b:int)-> bool:
  return arr[a].getDate() < arr[b].getDate()

def maintain_heap(arr:List[Virus], size:int, parent:int, compareFunction)-> None:
  left:int = parent * 2 + 1; right:int = parent * 2 + 2; heaper:int = parent

  if left < size and compareFunction(arr, left, heaper):
    heaper = left

  if right < size and compareFunction(arr, right, heaper):
    heaper = right

  if parent != heaper:
    arr[parent], arr[heaper] = arr[heaper], arr[parent]
    maintain_heap(arr, size, heaper, compareFunction)



def heapSort (arr:List[Virus], compareFunction)-> None:
  size:int = len(arr)
  idx:int = (size // 2) - 1
  while idx >= 0:
    maintain_heap(arr, size, idx, compareFunction)
    idx -= 1
  idx = size - 1
  while idx > 0:
    arr[idx], arr[0] = arr[0], arr[idx]
    maintain_heap(arr, idx, 0, compareFunction)
    idx -= 1

def heapAccessGT(objList:List[Virus])-> None:
  heapSort(objList, accessGT)

def heapAccessLT(objList:List[Virus])-> None:
  heapSort(objList, accessLT)

def heapDateLT(objList:List[Virus])-> None:
  heapSort(objList, dateLT)