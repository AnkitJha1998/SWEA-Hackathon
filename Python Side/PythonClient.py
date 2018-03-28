import serial
import _thread
import time
import numpy as np
import cv2

ard=serial.Serial('COM6',9600)

#----------------------------------------------------Case 1---------------------------------------------------

def check(b,c):
    for i in b:
        if c==i:
            return True
    return False
def choose1(data):
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
def choose2(data):
    
    str=ard.readline()
    str=str.decode('utf-8')
    print(str)
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
def image():
    detector=cv2.CascadeClassifier('harrcascade_frontalface_default.xml')
    cap=cv2.VideoCapture(0)
    while(True):
        ret,img=cap.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=detector.detectMiltiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('frame',img)
        if(cv2.waitKey(1)& 0xFF ==ord('q')):
            break


def choose3():
    print("\nYet to be figured out.\nThe Face recognition is under progress. Well if you would like to see the half-prepared recognition software then press w.\nIn camera window, press q to exit")
    choice=input()
    if(choice=='q'):
        image()
        


#----------------------------------------------------------------------------------------------------------------

choose=1
data="hello"

while(1):
    data=ard.readline()
    data=data.decode('utf-8')
    
    choose=int(input("\n1. Enter ID\n2. Check for Intruder alarm\n3. Face Recognition\n4. Exit\n\nChoose:"))
    if choose==1:
        choose1(data)
    elif choose==2:
        choose2(data)
    elif choose==3:
        choose3()
    elif choose==4:
        break;
print("Bye")
