import Serial
import _thread

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

    for i in range(1,4):
        a = input("Enter your Security number : ")
        if check(x,a) == True:
            print("Welcome ", a)
            break
        elif i<3:
            print("Incorrect Detail. You have ", (3-i), " chances")
        if i>=3:
            print("Intruder alert")
    return

#-------------------------------------------------------------------------------------------------------------
intruder=false;
def choose2():
    ard1=serial.Serial('COM8',9600)
    str=ard.readLine()
    if(str[0]=='1'):
        print("! ! ! Intruder Alert ! ! !")
        intruder=true;
    


choose=1
while(1):
    choose=int(input("\n1. Enter ID\n2. Check for Intruder alarm\n3. Face Recognition\n\4. Turn off Alarm(If Intruder Detected)n5. Exit\n\nChoose:"))
    if choose==1:
        choose1()
    elif choose==2:
        choose2()
    elif choose==3:
        choose3()
    elif choose==4:
        choose4()
    elif choose==5:
        break;
print("Bye")
