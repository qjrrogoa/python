'''
-논리연산자(이항연산자)의 결과값은 True,False이다.
and: and연산자(논리곱) 두 항이 참일때만 참이다 (~그리고)
or : or연산자(논리합) 두 항중의 하나라도  참이면 참(~또는 ,혹은)
not(단항연산자) : not연산자(논리부정) 단항이 참이면 거짓,거짓이면 참(~아니다)

-논리연산자의 우선 순위: not > and > or
※단락평가(short-circuit evalution)
 단락 평가는 첫 번째 항만으로 결과가 확실할 때 두 번째 항은 계산하지 않는 방법을 말한다.
 and는 첫째항이 거짓이면 두번째항은 계산안한다
 or는 첫째항이 참이면 두번째항을 계산 안한다
-산술 > 비교 >논리연산자순으로 우선순위가 적용됨.
'''

print("[논리 연산자]")
num1,num2 = 15,10
b= num1 > num2 and num1 == num2
print("{0} > {1} and {0} == {1}의 결과 : {2}".format(num1,num2,b))
b = True or False
print("{} or {}의 결과 {}".format(True,False,b))
print("[연산자 우선순위]")
b = 5 * 2 % 3 > 6 - 2 * 2 and 10 <= 6 * 2 or 5 * 3 != 10
print(b)

#※파이썬에는 xor연산자가 따로 없다. xor연산을 하려면 아래와 같은 방법으로 한다
#방법1] bool(값) ^ bool(값)
print("[파이썬의 XOR연산 첫번째]")
print(3 > 2 ^ 3 > 1)
print(bool(1) ^ bool(0))

#방법2] operator모듈의 xor함수 사용
import operator
print(operator.__file__)
print(dir(operator))
print(operator.xor(bool(1),bool(0)))
