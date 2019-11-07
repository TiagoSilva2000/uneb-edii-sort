import sys
sys.path.insert(1, '/home/ttiago/codes/ed2/trab1')

from typing import List
import time

from classes.Virus import Virus
from source.Selection import *
from source.Quick import *
from source.Merge import *
from source.Heap import *

def clearString(tempStr:str)-> str:
  newStr:str = ""
  for i in tempStr:
    if i == " ":
      break
    newStr += i
  return newStr

def createObjList()-> List:
  objList:List = []
  tempList:List[str] = []
  for virusLine in open("files/source/dados.csv", "r"):
    tempList = virusLine.split(";")
    tempList[-1] = clearString(tempList[-1])
    objList.append(Virus(tempList))
  return objList

def registerTime(functionToCall)-> float:
  objList:List = createObjList()

  t1Selec:float = time.time()
  functionToCall(objList)
  t2Selec:float = time.time()

  return (t2Selec - t1Selec)

def buildSelectionList (selecTimes:List[float])-> None:
  selecTimes.append(registerTime(selectionAccessGT))
  selecTimes.append(registerTime(selectionAccessLT))
  selecTimes.append(registerTime(selectionDateLT))

def buildQuickList (quickTimes:List[float])->None:
  quickTimes.append(registerTime(quickAccessGT))
  quickTimes.append(registerTime(quickAccessLT))
  quickTimes.append(registerTime(quickDateLT))

def buildMergeList (mergeTimes:List[float])->None:
  mergeTimes.append(registerTime(mergeAccessGT))
  mergeTimes.append(registerTime(mergeAccessLT))
  mergeTimes.append(registerTime(mergeDateLT))

def buildHeapList (heapTimes:List[float])->None:
  heapTimes.append(registerTime(heapAccessGT))
  heapTimes.append(registerTime(heapAccessLT))
  heapTimes.append(registerTime(heapDateLT))
