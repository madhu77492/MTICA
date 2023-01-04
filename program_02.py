def printDay(d):
    if (d==1):
        return 'Sunday'
    if (d==2):
        return 'Monday'
    if (d==3):
        return 'Tuesday'
    if (d==4):
        return 'Wednesday'
    if (d==5):
        return 'Thursday'
    if (d==6):
        return 'Friday'
    if (d==7):
        return 'Saturday'

for i in range(3):
    inpNum=int(input())
    print(printDay(inpNum))
    
