# -*- coding: utf-8 -*-



def myCon(p):
    temp=p
    data=open("myCon.csv",'a')
    while temp != 1:
        if temp%2==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/2
        elif temp%3==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/3
        elif temp%5==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/5
        elif temp%7==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/7
        elif temp%11==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/11
        elif temp%13==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/13
        elif temp%17==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/17
        elif temp%19==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/19
        elif temp%23==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/23
        elif temp%29==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/29
        elif temp%31==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/31
        elif temp%37==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/37
        elif temp%41==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/41
        elif temp%43==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/43
        elif temp%47==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/47 #15
        
        else:
            data.write(str(temp)+',')
            print(temp)
            temp=temp*53+1 #16
    if temp==1:
        data.write(str(temp)+'\n')
        print(temp)
    print(temp)







def facReturn(a,b):
    tempc=a
    while tempc<=b:
        print(str(factor(tempc)))
        tempc=tempc+1

def collatzFactor(p):
    temp=p
    while temp != 1:
        if temp%2==0:
            print(factor(temp))
            temp=temp/2
        else:
            print(factor(temp))
            temp=temp*3+1
    print(temp)

def collatz(p):
    temp=p
    while temp != 1:
        if temp%2==0:
            print(temp)
            temp=temp/2
        else:
            print(temp)
            temp=temp*3+1
    print(temp)

def collatzTextappend(p):
    temp=p
    data=open("3n+1.csv",'a')
    while temp != 1:
        if temp%2==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/2
        else:
            data.write(str(temp)+',')
            print(temp)
            temp=temp*3+1
    if temp==1:
        data.write(str(temp)+'\n')
        print(temp)
    print(temp)

def collatzbTextappend(p):
    temp=p
    data=open("5n+1.csv",'a')
    while temp != 1:
        if temp%2==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/2
        elif temp%3==0:
            data.write(str(temp)+',')
            print(temp)
            temp=temp/3
        else:
            data.write(str(temp)+',')
            print(temp)
            temp=temp*5+1
    if temp==1:
        data.write(str(temp)+'\n')
        print(temp)
    print(temp)

def collatzTextAppend(p):
    temp=1
    while temp<=p:
        collatzTextappend(temp)
        temp=temp+1

def collatzbTextAppend(p):
    temp=1
    while temp<=p:
        collatzbTextappend(temp)
        temp=temp+1

def collatzb(p):
    temp=p
    while temp != 1:
        if temp%2==0:
            print(temp)
            temp=temp/2
        elif temp%3==0:
            print(temp)
            temp=temp/3
        else:
            print(temp)
            temp=temp*5+1
    print(temp)
    
def collatzc(p):
    temp=p
    while temp != 1:
        if temp%2==0:
            print(temp)
            temp=temp/2
        elif temp%3==0:
            print(temp)
            temp=temp/3
        elif temp%5==0:
            print(temp)
            temp=temp/5
        else:
            print(temp)
            temp=temp*7+1
    print(temp)
def collatzd(p):
    temp=p
    while temp != 1:
        if temp%2==0:
            print(temp)
            temp=temp/2
        elif temp%3==0:
            print(temp)
            temp=temp/3
        elif temp%5==0:
            print(temp)
            temp=temp/5
        elif temp%7==0:
            print(temp)
            temp=temp/7
        else:
            print(temp)
            temp=temp*11+1
    print(temp)
def collatze(p): # 277 루프발생
    temp=p
    while temp != 1:
        if temp%2==0:
            print(temp)
            temp=temp/2
        elif temp%3==0:
            print(temp)
            temp=temp/3
        elif temp%5==0:
            print(temp)
            temp=temp/5
        elif temp%7==0:
            print(temp)
            temp=temp/7
        elif temp%11==0:
            print(temp)
            temp=temp/11
        else:
            print(temp)
            temp=temp*13+1
    print(temp)
def collatzf(p):
    temp=p
    while temp != 1:
        if temp%2==0:
            print(temp)
            temp=temp/2
        elif temp%3==0:
            print(temp)
            temp=temp/3
        elif temp%5==0:
            print(temp)
            temp=temp/5
        elif temp%7==0:
            print(temp)
            temp=temp/7
        elif temp%11==0:
            print(temp)
            temp=temp/11
        elif temp%13==0:
            print(temp)
            temp=temp/13
        else:
            print(temp)
            temp=temp*17+1
    print(temp)
def collatzg(p):
    temp=p
    while temp != 1:
        if temp%2==0:
            print(temp)
            temp=temp/2
        elif temp%3==0:
            print(temp)
            temp=temp/3
        elif temp%5==0:
            print(temp)
            temp=temp/5
        elif temp%7==0:
            print(temp)
            temp=temp/7
        elif temp%11==0:
            print(temp)
            temp=temp/11
        elif temp%13==0:
            print(temp)
            temp=temp/13
        elif temp%17==0:
            print(temp)
            temp=temp/17
        else:
            print(temp)
            temp=temp*19+1
    print(temp)
def collatzh(p):
    temp=p
    while temp != 1:
        if temp%2==0:
            print(temp)
            temp=temp/2
        elif temp%3==0:
            print(temp)
            temp=temp/3
        elif temp%5==0:
            print(temp)
            temp=temp/5
        elif temp%7==0:
            print(temp)
            temp=temp/7
        elif temp%11==0:
            print(temp)
            temp=temp/11
        elif temp%13==0:
            print(temp)
            temp=temp/13
        elif temp%17==0:
            print(temp)
            temp=temp/17
        elif temp%19==0:
            print(temp)
            temp=temp/19
        else:
            print(temp)
            temp=temp*23+1
    print(temp)
def collatzi(p):
    temp=p
    while temp != 1:
        if temp%2==0:
            print(temp)
            temp=temp/2
        elif temp%3==0:
            print(temp)
            temp=temp/3
        elif temp%5==0:
            print(temp)
            temp=temp/5
        elif temp%7==0:
            print(temp)
            temp=temp/7
        elif temp%11==0:
            print(temp)
            temp=temp/11
        elif temp%13==0:
            print(temp)
            temp=temp/13
        elif temp%17==0:
            print(temp)
            temp=temp/17
        elif temp%19==0:
            print(temp)
            temp=temp/19
        elif temp%23==0:
            print(temp)
            temp=temp/23
        else:
            print(temp)
            temp=temp*29+1
    print(temp)
def collatzj(p):
    temp=p
    while temp != 1:
        if temp%2==0:
            print(temp)
            temp=temp/2
        elif temp%3==0:
            print(temp)
            temp=temp/3
        elif temp%5==0:
            print(temp)
            temp=temp/5
        elif temp%7==0:
            print(temp)
            temp=temp/7
        elif temp%11==0:
            print(temp)
            temp=temp/11
        elif temp%13==0:
            print(temp)
            temp=temp/13
        elif temp%17==0:
            print(temp)
            temp=temp/17
        elif temp%19==0:
            print(temp)
            temp=temp/19
        elif temp%23==0:
            print(temp)
            temp=temp/23
        elif temp%29==0:
            print(temp)
            temp=temp/29
        else:
            print(temp)
            temp=temp*31+1
    print(temp)

def factor(x):
    d=2
    result=[]
    while d<=x:
        if x%d==0:
            result.append(d)
            x=x/d
        else:
            d=d+1
    return result

def inHow(p,q):
    temp=0
    while p%q==0:
        temp=temp+1
        p=p/q
    return temp

def inHowExcel(p,q):
    print("ex)./data.txt")
    address=input("저장할 주소 및 이름:")
    data=open(address,'w')
    temp=1
    while temp<=p:
        data.write(str(inHow(temp,q))+'\n')
        print(inHow(temp,q))
        temp=temp+1
    data.close()




