def removeElement(oldList, remove):
    for i in range(len(oldList)):
        if oldList[i] == remove:
            oldList.pop(i)
            return True

    return False

