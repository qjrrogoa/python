#정수형(int)은 소수점이 없는 숫자를 의미
#100 -100등
def pprint(value):
    print("value : ",value,sep="",end=", ")
    print("type : ",type(value),sep="")
a=100
pprint(a)
#파이썬 3에서는 정수 / 정수 = 실수이다(파이썬 2 정수 / 정수 = 정수)
b = 5/2
pprint(b)

c=int(b)
pprint(c)

'''
※정수는 10진수 이외에도 2진수, 8진수, 16진수로 표현
2진수 : 숫자 앞에 0b(B)를 붙이며 0과 1을 사용.
8진수 : 숫자 앞에 0o(O)를 붙이며 0부터 7까지 사용
16진수 : 숫자 앞에 0x(X)를 붙이며 0부터 9, A부터 F까지 사용(소문자 a부터 f도 가능)
'''
print('[각 진수로 숫자 표현하기]')
print("2진수 : ",0b10)
print("8진수 : ",0o10)
print("16진수 : ",0x10)

#int 타입의 숫자는 크기에 제한이 없다. 즉, 아무리 큰 정수라도 표현할 수 있다.
d=40284*12425
pprint(d)

#실수형(float)은 소수점이 있는 숫자를 의미
#10.0,-3.14등
#실수와 정수의 연산결과는 실수이다
a=10
b=3.5
pprint(b)
pprint(a+b)

print("[0.1+0.2 연산결과 : 0.3이 아니다]")
a=0.1
b=0.2
print(a+b) #0.30000000000000004

print("[정수를 실수로 변환하기]")
pprint(float(1+2))