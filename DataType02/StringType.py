print('[문자열 만들기1]')
print('Hello World')

print('[문자열 만들기2]')
print("Hello World")

print('문자열 만들기3]')
print(
    '''
    Hello World
    Hi Python!!!
    Good Luck To you!
    '''
)

print('문자열 만들기4]')
print(
"""
Hello World
Hi Python!!!
Good Luck To you!
"""
)

#'''와 """안에는 '와 " 둘다 넣을 수 있다
print('''
Hello World
Hi "Python"!!!
Good Luck To 'you'!
''')

#문자열 길이 구하기
print("[len()함수로 문자열 길이 구하기]")
print("hello ",len("hello"))
print("안녕하세요 ",len("안녕하세요"))

'''
※유니코드 문자열을 인코딩없이 그대로 파일에 쓰거나 다른 시스템으로 
  네트워크 전송을 할 수는 없다. 
  왜냐하면 유니코드 문자열은 단순히 문자셋의 규칙이기 때문이다.
  파일에 쓰거나 다른 시스템으로 유니코드 문자열을 전송하기 위해서는 
 바이트로 변환해야만 한다
'''
#encode("문자셋") : 유니코드 문자열을 바이트 문자열로 만드는 함수
#문자셋를 생략하면 디폴트 값인 utf-8로 동작.
print("[encode()함수로 문자열을 바이트 문자열로 변경]")
print("hello")
print('hello'.encode(encoding="utf-8"))
print(len('hello'.encode(encoding="utf-8"))) #영어는 1바이트

print("안녕하세요")
print('안녕하세요'.encode(encoding="utf-8"))
print(len('안녕하세요'.encode(encoding="utf-8"))) #한글은 3바이트

#decode(): 인코딩된 바이트 문자열을 (유니코드)문자열로 변환하는 함수
print("[decode()함수로 바이트 문자열을 일반 문자열로 변경")
print('hello'.encode().decode())
print('안녕하세요'.encode().decode())

#문자열로 연결하기 + 사용
print("[+로 문자열 연결하기]")
print("hello " + 'world')
#print("hello "+ 100)에러
print("hello "+str(100))

#문자열 반복하기 : * 사용
#0이나 음수를 곱하면 빈 문자열 단, 실수는 곱할 수 없다(에러)
print("[*로 문자열 반복하기]")
print("파이썬 "*3)


