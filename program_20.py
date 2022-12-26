def count_specialcharacter(s):
    specialcharacter=0
    for i in s:
        if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghjiklmnopqrstuvwxyz1234567890':
            specialcharacter+=1
    return specialcharacter

str1=input()
a=count_specialcharacter(str1)
print("no of  consonant in:'",str1,"' is",a)
