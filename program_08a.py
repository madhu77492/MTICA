'''Lst=[10,15,20,25,30,35,40,45]
120)Use list comprehension to construct a list
with square each element in the list, if the square is graeater than 50.'''
##Lst=[10,15,20,25,30,35,40,45]
##ans=[]
##for i in Lst:
##    if i*i>50:
##        ans.append(i*i)
##print(ans)


Lst=[10,15,20,25,30,35,40,45]
ans=[i*i for i in Lst if i*i>50]

print(ans)
