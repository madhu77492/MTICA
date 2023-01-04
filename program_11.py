def CalculateCubic():
    i=1;
    while True:
        yield i*i*i
        i+=1
for num in CalculateCubic():
    if num>1000:
        break
    print(num)
