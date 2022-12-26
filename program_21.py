def extract_specialcharacter(s):
    specialcharacter=''
    for i in s:
        if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghjiklmnopqrstuvwxyz1234567890':
            specialcharacter+=i
    return specialcharacter

str1=input()
a=extract_specialcharacter(str1)
print("specialcharacters in:'",str1,"' is",a)
