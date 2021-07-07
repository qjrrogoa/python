num1 = 100
print("[if문 형식 첫번째로 짝/홀수 판단]")
if num1 % 2 == 0:
    print("짝수")
if num1 % 2 != 0:
    print("홀수")

print("[if문 형식 두번째로 짝/홀수 판단]")
#조건식 한번만 실행됨.
if num1 % 2 == 0:
    print("짝수")
else:
    print("홀수")

#[조건부 표현식 다른 언어에서는 삼항연산자라 함]
'''
if~else문과 같다.
코드를 짧게 표현할 때 주로 사용(if ~ else문 대신에)
구문]
변수 = 값 if 조건문 else 값
'''
print("[조건부 표현식(삼항연산자)로 짝/홀수 판단]")
result = "짝수" if num1 % 2 ==0 else "홀수"
print(result)

if num1 % 2 == 0:
    print("짝수")
print("num1는",num1)#if문과 무관
'''
else :
    print("홀수")
'''
#문] 한 문자를 입력받아 숫자인지 아닌지
# if ~ else문과 조건부 표현식을 이용하여 판단하여라.
print("숫자" if '0' <= input("한 문자를 입력 : ") <= '9' else "문자")



