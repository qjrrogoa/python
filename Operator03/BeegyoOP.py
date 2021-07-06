'''
-비교연산자(이항연산자)의 결과는
True아니면 False(bool값)
> : ~보다 크다
>=: ~보다 크거나 같다
< : ~보다 작다
<=: ~보다 작거나 같다
!=: 같지 않다
==: 같다
-비교연산자는 모두 우선순위가 같다
-산술연산자가 비교 연산자보다 우선 순위가 높다
-비교 연산자를 사용한 식은 비교식
'''
print("[숫자 비교]")
num1 = num2 = 10
print(num1 >= num2)
b = num1 <= num2
print("{} <= {}의 결과 {}".format(num1,num2,b))

b = num1 != num2
print("{} != {}의 결과 {}".format(num1,num2,b))

#숫자뿐만 아니라 문자열도 ==와 != 여난자로 비교할 수 있다
#물론 대소도 비교 가능. 이때는 아스키코드 혹은 유니코드값으로 비교한다.
'''    
아스키 코드:1byte로 표현할 수 있는 문자
(영문자 와 숫자)
십진수로 정의한 값을 아스키 코드라 함.
예]A의 아스키 코드값:65(이진수-1000001)
키보드에서 A라고 치면 컴퓨터 메모리에 
1000001로 저장됨.
소문자 a는 아스키 코드값이 97

유니코드:1BYTE로 표현이 안되는 문자
(한글이나 한자등)
은 3BYTE가 필요하다.\\x16진수로 정의한 값을
유니코드라 한다.
'''
print("[문자열 비교]")
print("PYTHON" == "python")

print("ABC" < "ABD") #False

b = 15 % 3 * 2 + 4 > (10-2) * 4 != True
print("b의 값",b)

# ==,!=는 값 자체를 비교하고, is, is not은 객체(object)를 비교
# id()함수: 객체의 주소값 반환하는 함수
print("[==와 is 연산자]")
a=1
b=1.0
print(a == b)
print(a is b)
print("a의 주소 : {}, b의 주소 : {}".format(id(a),id(b)))

#bool()함수 : 정수, 실수 혹은 문자열, 객체등을 bool로 만들 때 사용
# 0 혹은 0.0이 그리고 '' 혹은 빈 객체를 제외한 모든 정수, 실수, 문자열 객체등은 True
# 빈 리스트 [] bool로 변환시 False로 변환됨
a=0.0
b=False
print(a==b)
print(a is b)
print(bool(a) is b)

print("0 : {}, 0.0 : {}, 빈 문자열 : {}, 빈 객체 : {}".format(bool(0),bool(0.0),bool(''),bool([])))
print("-10 : {}, 3.14 : {}, 'HELLO' : {}, 객체 : {}".format(bool(-10),bool(3.14),bool('HELLO'),bool([1,2,3])))

#빈 리스트를 bool값과 비교시에는 bool()함수로 변환 후 비교
#단, 빈 리스트를 not함께 쓸때는 bool()변환 불필요
a = []
print(a == b) #False
print(bool(a)==b)

print((not a) == b)


