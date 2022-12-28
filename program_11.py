#remove empty string
lst1=["Sedan","SUV", "", "", "Pickup",'',' ']

ans=[]
for i in lst1:
    if i:
        ans.append(i)

print(ans)
