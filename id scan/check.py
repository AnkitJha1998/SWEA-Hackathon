def check(b,c):
    for i in b:
        if c==i:
            return True
    return False

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
