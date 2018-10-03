# -*- coding: utf-8 -*-

from function import *


def cSub():
    print("n까지의 수를 소인수분해를 했을 시 요소 갯수를 구하려면 a를 입력")
    print("콜라츠 추측을 텍스트로 저장하려면 b를 입력"
    subInput=input()
    if subInput=="a":
        number1=input("입력:")
        number1=int(number1)
        number2=input("요소:")
        number2=int(number2)
        inHowExcel(number1,number2)
    elif subInput=="b":
        p=input("대입할 숫자:")
        p=int(p)
        collatzText(p)
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













