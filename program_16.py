def count_specialcharacters(s):
    n_specialcharacter=0
    for i in s:
        if i not in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            n_specialcharacter+=1
    return n_specialcharacter

str1=input()
a=count_specialcharacters(str1)
print("No of specialcharacters is :'",str1,"' is",a)
