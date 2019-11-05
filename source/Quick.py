import sys
sys.path.insert(3, '/home/ttiago/codes/ed2/trab1')

from source.fileHandler import dateLT, accessGT, accessLT
import random

def swap(listy, i, j):
    aux = listy[i]
    listy[i] = listy[j]
    listy[j] = aux


def quickSort(listy, initialPosition, finalPosition, cmpFunction):
    if initialPosition < finalPosition :
        pivo = partition(listy, initialPosition, finalPosition, cmpFunction)
        quickSort(listy, initialPosition, (pivo-1), cmpFunction)
        quickSort(listy, (pivo + 1), finalPosition, cmpFunction)

def partition(listy, initialPosition, finalPosition, cmpFunction):
    pivo = listy[initialPosition]
    pivoPlace = initialPosition
    walker = initialPosition + 1

    while walker <= finalPosition:
        if(cmpFunction(listy, walker, pivoPlace)):
            pivoPlace+=1
            swap(listy, pivoPlace, walker)
        walker+=1

    swap(listy, initialPosition, pivoPlace)

    return pivoPlace

def quickDateLT(listy):
  quickSort(listy, 0, len(listy)-1, dateLT)

def quickAccessLT(listy):
  quickSort(listy, 0, len(listy)-1, accessLT)

def quickAccessGT(listy):
  quickSort(listy, 0, len(listy)-1, accessGT)