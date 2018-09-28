# -*- coding: utf-8 -*-

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
def collatze(p):
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
    data=open('./data.txt','w')
    temp=1
    while temp<=p:
        data.write(str(inHow(temp,q))+'\n')
        print(inHow(temp,q))
        temp=temp+1
    data.close()

def cSub():
    print("콜라츠 추측의 pn+1을 실행하시려면 a를 입력")
    subInput=input()
    if subInput=="a":
        number1=input("대입할 숫자를 입력:")
        number1=int(number1)
        number2=input("몇번째 소수입니까?:")
        inHowExcel(number1,number2)
        number2=int(number2)
    else:
        print("없는 메뉴입니다. 다시 선택해 주십시오")
        cSub()
     
def main():
    print("소인수분해를 하시려면 a를 입력")
    print("우박수열을 확인하시려면 b를 입력")
    print("텍스트 파일로 저장하시려면 c를 입력")
    mainInput=input()
    
    if mainInput=="a":
        number=input("입력:")
        facReturn(int(number),int(number))
        main()
        
    elif mainInput=="b":
        number=input("입력:")
        collatz(int(number))
        main()
        
    elif mainInput=="c":
        cSub()
        
    else:
        print("없는 메뉴입니다. 다시 선택해 주십시오")
        main()
        
main()













