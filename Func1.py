#함수 정의 하기전에 함수 호출하기
#파이썬은 코드를 순차적으로 실행하기 때문에 함수 정의전에 호출하면 에러
#helloPython()

def helloPython():
    print("Hello Python")
    return "hi"
#함수 호출하기
helloPython()
print(helloPython()) #반환값이 없을때는 None
def empty():
    pass

print(empty())#None

#함수 독스트링 사용하기
def printMessage(msg):
    '''
        함수 독스트링 : 주석처럼 사용할 수 있으나 하나의 명령문이다.
        문자열을
        :param msg : 입력받은 문자열
        :return : 반환값은 없다
    '''
    msg ="입력값 : {}".format(msg)
    print(msg)


printMessage("Hello Python")
print("[함수 독스트링 출력하기")
print(printMessage.__doc__)

#함수 결과값 반환하기
def add(a,b):
    result = a+b
    return result
    print("실행 안됨")

result = add(10,20)
print(result)
print(add(10,20))

def entrance(age):
    if not 20 <= age <= 40:
        print("입장 불가")
        return
    print("즐거운 시간 보내세요")

entrance(10)
entrance(20)
entrance(40)

def add(x,y):
    c=x+y
    return c,x,y # 튜플 반환

r = add(10,20)
print(r)

z,x,y=add(100,200)
print('{}+{}={}'.format(x,y,z ))