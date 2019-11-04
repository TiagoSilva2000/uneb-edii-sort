def swap(listy, i, j):
    aux = listy[i]
    listy[i] = listy[j]
    listy[j] = aux


def quickSort(listy, initialPosition, finalPosition):
    if initialPosition < finalPosition :
        pivo = partition(listy, initialPosition, finalPosition)
        quickSort(listy, initialPosition, (pivo-1))
        quickSort(listy, (pivo + 1), finalPosition)

def partition(listy, initialPosition, finalPosition):
    pivo = listy[initialPosition]
    pivoPlace = initialPosition
    walker = initialPosition + 1

    while walker <= finalPosition:
        if(listy[walker] < pivo):
            pivoPlace+=1
            swap(listy, pivoPlace, walker)
        walker+=1

    swap(listy, initialPosition, pivoPlace)

    return pivoPlace
