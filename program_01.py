def checkLength(n):
    lst=n.split()
    return [len(i) for i in lst]
inp=input()
print(*checkLength(inp))
