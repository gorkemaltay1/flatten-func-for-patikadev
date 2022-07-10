ourList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
newList = []
def flatten(flatList):
    for i in flatList:
        if isinstance(i, list):
            flatten(i)
        else:
            newList.append(i)

flatten(ourList)
print(newList)