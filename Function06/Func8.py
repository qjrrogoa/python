print('[지역변수]')#함수안에서 선언된 변수:지역변수
def add(*args):
    total = sum(args)
    print('{}부터 {}까지 누적합:{}'.format(args[0],args[len(args)-1],total))

add(*[i for i in range(1,11)])
#print(total)#NameError: name 'total' is not defined
#print(args)#NameError: name 'args' is not defined
print('[전역변수]')#스크립트 파일(.py) 전체에서 사용할 수 있는 변수
a=10 #전역변수
b=1000
def add2():
    total=0
    print('전역변수:',b)#함수 밖 b 사용.권장하지 않는다
    a = int(input('숫자 입력?')) + 1  # a는 지역변수
    #global a #global 키워드는 쓰지말자.함수가 외부변수에 의존하니까
    #a=int(input('숫자 입력?'))+1#a는 전역변수 즉 함수밖의 a를 사용
    for i in range(1,a):
        total+=i
    print('{}부터 {}까지 누적합:{}'.format(1,a-1, total))

add2()
print('함수 밖의 a출력:',a)