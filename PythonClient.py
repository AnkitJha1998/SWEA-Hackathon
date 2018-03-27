import serial
import _thread
import time

ard=serial.Serial('COM6',9600)

#----------------------------------------------------Case 1---------------------------------------------------

def check(b,c):
    for i in b:
        if c==i:
            return True
    return False
def choose1():
    file = open('dataset.txt','r')
    x = file.readlines()
    x = [j.rstrip('\n') for j in x]
    counter=False
    for i in range(1,4):
        a = input("Enter your Security number : ")
        if check(x,a) == True:
            print("Welcome ", a)
            counter=True
            break
        elif i<3:
            print("Incorrect Detail. You have ", (3-i), " chances")
        if i>=3:
            print("! ! ! Intruder suspected ! ! !")
    if counter==True :
        str=ard.readline()
        str=str.decode('utf-8')
        if str[0]=='2':
            print('! ! ! Intruder Alert ! ! !')
            while(str[0]!='0'):
                str=ard.readLine()
                if str[0]=='0':
                   break;
        strWrite="1;\n"
        ard.write(strWrite.encode("utf-8"))
        print("\nAccess Granted for thirty seconds.\n\n")
        time.sleep(30)
        strWrite="2;\n"
        ard.write(strWrite.encode('utf-8'))   
    return

#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------Case 2-----------------------------------------------------

intruder=False
def choose2():
    
    str=ard.readline()
    str=str.decode('utf-8')
    print(str[0])
    if str[0]=='2' :
        print("! ! ! Intruder ALERT ! ! !")
        intruder=True
        while(intruder!=False):
            str1=ard.readline()
            str1=str1.decode('utf-8')
            if str1[0]=='0':
                intruder=False
                break;
    return
    
#---------------------------------------------------------------------------------------------------------------


#----------------------------------------------Case 3------------------------------------------------------------
def choose3():
    print("Yet to be figured out")    


#----------------------------------------------------------------------------------------------------------------

choose=1
while(1):
    choose=int(input("\n1. Enter ID\n2. Check for Intruder alarm\n3. Face Recognition\n4. Exit\n\nChoose:"))
    if choose==1:
        choose1()
    elif choose==2:
        choose2()
    elif choose==3:
        choose3()
    elif choose==4:
        break;
print("Bye")
