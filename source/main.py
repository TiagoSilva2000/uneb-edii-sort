from typing import TYPE_CHECKING
from typing import List, TextIO, Dict
from Virus import Virus
from fileHandler import buildSelectionList
import time

# Declaration:
t1merge:float = 0; t2merge:float = 0
t1quick:float = 0; t2quick:float = 0
t1heap:float = 0; t2heap:float = 0
selecTimes:List[float] = []
mergeTimes:List[float] = []
quickTimes:List[float] = []
heapTimes:List[float] = []

buildSelectionList(selecTimes)

log = open("../log/selection.txt", "a")

log.write("[Selection Sort] (AccessionGT - {}) (AccessionLT - {}) (DateLT - {})\n"
          .format(selecTimes[0], selecTimes[1], selecTimes[2]))
log.close()