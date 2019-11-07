import sys
sys.path.insert(1, '/home/ttiago/codes/ed2/trab1')

from typing import TYPE_CHECKING
from typing import List, TextIO, Dict
from classes.Virus import Virus
from source import fileHandler
import time

def writeToLog(sortName:str, sortArray:List):
  log = open("files/log/" + sortName + ".txt", "a")
  log.write("[{} Sort] (AccessionGT - {}) (AccessionLT - {}) (DateLT - {})\n"
            .format(sortName, sortArray[0], sortArray[1], sortArray[2]))
  log.close()

# def accessLT(arr:List[Virus], a:int, b:int)-> bool:
#   return arr[a].getAccess() < arr[b].getAccess()

# def accessGT(arr:List[Virus], a:int, b:int)-> bool:
#   return arr[a].getAccess() > arr[b].getAccess()

# def dateLT(arr:List[Virus], a:int, b:int)-> bool:
#   return arr[a].getDate() < arr[b].getDate()

# Declaration:
t1merge:float = 0; t2merge:float = 0
t1quick:float = 0; t2quick:float = 0
t1heap:float = 0; t2heap:float = 0
selecTimes:List[float] = []
mergeTimes:List[float] = []
quickTimes:List[float] = []
heapTimes:List[float] = []

fileHandler.buildSelectionList(selecTimes)
writeToLog("Selection", selecTimes)

fileHandler.buildHeapList(heapTimes)
writeToLog("Heap", heapTimes)

fileHandler.buildMergeList(mergeTimes)
writeToLog("Merge", mergeTimes)

fileHandler.buildQuickList(quickTimes)
writeToLog("Quick", quickTimes)