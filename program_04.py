def PrintSunday():
    print('You chose Sunday!\n')
    return
def PrintMonday():
    print('You chose Monday!\n')
def PrintTuesday():
    print('You chose Tuesday!\n')
def PrintWednesday():
    print('You chose Wednesday!\n')
def PrintThursday():
    print('You chose Thursday!\n')
def PrintFriday():
    print('You chose Friday!\n')
def PrintSaturday():
    print('You chose Saturday!\n')
def choice():
    print("1:Sunday")
    print("2:Monday")
    print("3:Tuesday")
    print("4:Wednesday")
    print("5:Thursday")
    print("6:Friday")
    print("7:Saturday")
    print("8:Quit")
    return
DaySelect={1:PrintSunday,2:PrintMonday,3:PrintTuesday,4:PrintWednesday,5:PrintThursday,6:PrintFriday,7:PrintSaturday}
selection=0
while True:
    if selection==8:break
    choice()
    selection=int(input("select a day option:"))
    if (selection>=0) and (selection<8):
        DaySelect[selection]()
    
    
