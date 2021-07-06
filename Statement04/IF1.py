if not 0:
    print("0은 False다")
if not None:
    print("None은 False다")
if not "":
    print("''은 False다")
if not[]:
    print('[]은 False다')

#조건식은 모든 식이 될 수 있다.
num1 = 10
if num1:
    print("num1은 ",num1)
if num1 % 2:
    print("num1 % 2의 값은 ",num1%2)
if num1 % 2 == 0:
    print("{}은 짝수다".format(num1))
if num1 % 2 == 0 and num1 >= 10:
    print("%d는 짝수이고 10보다 크거나 같다" % num1)

#파이썬에서 조건시을 수학에서 사용하는 방식으로 간편화 할 수도 있다.
if 5 < num1 < 15 :#num1 > 5 and num1 < 15와 같다
    print("{}는 5보다 크고 15보다 작다".format(num1))

#if 조건식 :
#조건식 들역쓰기 한 다음줄에 코드가 없으면 에러 즉 pass 생략시 에러
if num1 % 2 == 0:
    pass

if num1 % 2 != 0:
    print("num1은 %d다" % num1)
    print("%d는 홀수다" % num1)

'''
ord(문자) : 문자의 아스키코드나 유니코드값을 반환
chr(숫자) : 숫자(아스키코드값 혹은 유니코드값)에 대응하는 문자를 반환
'''
print("[문자를 아스키(유니)코드로 변환 : ord(문자)]",ord('가'),sep="\n")
print("[문자를 아스키(유니)코드를 문자로 변환 : chr(문자)]",chr(44032),sep="\n")
code = ord(input("한 문자를 입력하세요 : "))
print(code)
print(code >= ord('B'))
'''
문] 사용자가 입력한 문자가 숫자인지 판단하여라
"숫자면 숫자입니다"라고 출력하여라
숫자가 아니면 "숫자가 아닙니다"라고 출력하여라
'''
if('0' <= chr(code) <= '9'):
    print("숫자입니다.")

