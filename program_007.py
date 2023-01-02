sample_dict={
    "name":"Mp",
    "age":22,
    "salary":80000,
    "city":"New york"}
keys=["name","salary"]


d=dict()
for i in sample_dict.keys()-keys:
    d[i]=sample_dict[i]
print(sample_dict)


