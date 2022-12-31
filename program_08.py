fo1=open(r"D:\Python_Practice31\Day9\Madhu2.txt","r")
fo2=open(r"D:\Python_Practice31\Day9\Madhu.txt","w+")

temp=fo1.read()
fo2.write(temp)

fo1.close()
fo2.close()

print("File copied")
