import sys
sys.path.insert(1, '/home/ttiago/codes/ed2/trab1/source')
from typing import List
from classes.Virus import Virus

def accessLT(arr:List[Virus], a:int, b:int)-> bool:
  return arr[a].getAccess() < arr[b].getAccess()

def accessGT(arr:List[Virus], a:int, b:int)-> bool:
  return arr[a].getAccess() > arr[b].getAccess()

def dateLT(arr:List[Virus], a:int, b:int)-> bool:
  return arr[a].getDate() < arr[b].getDate()








def mergeSort (objList:List[Virus], cmpFunction):
  pass

def mergeAccessGT(objList:List[Virus]):
  mergeSort(objList, accessGT)

def mergeAccessLT(objList:List[Virus]):
  mergeSort(objList, accessLT)

def mergeDateLT(objList:List[Virus]):
  mergeSort(objList, dateLT)
