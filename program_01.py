string='''
practice problems for List Com pre hension in Python
'''

wordsLst=string.split(' ')
print(wordsLst)
wordsLst=[i.strip("\n") for i in wordsLst ]
print(wordsLst)
ans={i:len(i) for i in wordsLst }
print(ans)
