import sys
print("coming through stdout")
save_stdout=sys.stdout
fh=open(r"D:\Python_Practice31\Day18\mp1.txt","w")
sys.stdout=fh
print("This line goes to mp1.txt")
print(input())
sys.stdout=save_stdout
fh.close()
