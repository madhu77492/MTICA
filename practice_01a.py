def printSeriesIncreasing(ch,n):
    assert(n>=0),'INVALID'
    for i in range(n,0,-1):
        print(ch*i)
    
ch=input()
n=int(input())
try:
    printSeriesIncreasing(ch,n)
except AssertionError as a:
    print(a)


