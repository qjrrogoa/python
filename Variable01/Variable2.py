import sys
print(sys.getrefcount(2021))
x=2021
print(sys.getrefcount(2021))
y=2021
print(sys.getrefcount(2021))
# is 연산자 : 객체가 같은 타입인지 판단하는 연산자
print(x is y)