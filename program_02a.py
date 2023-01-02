def frequencyDict(s): 
    frequencyDict=dict()
    for i in s:
        if i in frequencyDict:
            frequencyDict[i]+=1
        else:
            frequencyDict[i]=1
    return frequencyDict

def formatOutput(d):
    for i in sorted(d,reverse=True):
        print(i,d[i])
    

n=int(input())
for i in range(n):
    inpstr=input()
    formatOutput(frequencyDict(inpstr))
