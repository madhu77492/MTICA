def remove_Duplicates(s):
    temp=''
    for i in s:
        if i not in str2:
            str2 +=i
            #print (str2)
    return str2

str1=input("Enter your text: ")
print("without duplicate is: ",remove_Duplicates(str1))
