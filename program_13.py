def extract_vowel(s):
    temp_vowel=''
    for i in s:
        print("i=",i)
        if i in 'AEIOUaeiou':
            temp_vowel+=i
            print("i:",i,"temp_vowel:",temp_Vowel)
    return temp_vowel

str1=input("Enter the string:")
str=input()
a=extract_vowel(str1)
print("vowel:",a)
