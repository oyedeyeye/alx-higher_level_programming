#!/usr/bin/python3
def best_score(a_dictionary):
    if bool(a_dictionary):
        dictList = list(a_dictionary.items())
        max = dictList[0][1]
        for i in range(len(dictList)):
            if dictList[i][1] > max:
                max = dictList[i][1]

        for j in range(len(dictList)):
            if dictList[j][1] == max:
                return dictList[j][0]
    return None
