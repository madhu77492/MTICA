'''Lst=[10,15,20,25,30,35,40,45]
120)Use list comprehension to construct a new list
with square root of each item.'''
##Lst=[10,15,20,25,30,35,40,45]
##ans=[]
##for i in Lst:
##    ans.append(i+6)
##print(ans)


Lst=[10,15,20,25,30,35,40,45]
ans=[i*(1/2) for i in Lst]

print(ans)
