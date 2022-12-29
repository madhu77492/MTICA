num1=input("Enter a number:")
num2=input("Enter a number:")

try:
    res=int(num1)/int(num2) #Execute with num2=non zero and zero 
except ZeroDivisionError:
    print("Exception handled by Madhu")
except ValueError:
    print("Exception handled by MP")
except Exception as ob:
    print (ob)
else:
    print (num1, '/' ,num2, '=',res)
finally:
    print("Thanks")

print("visit again at python class at MTICA" )
