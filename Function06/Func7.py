#남다 표현식(함수)
print('[람다함수를 사용하지 않고 def 키워드로 함수 정의하여 사용하기]')
def plus100(arg):
    return arg+100
print('value:{},type:{}'.format(plus100,type(plus100)))
#리스트 [1,2,3,4,5]의 각 요소에 plus100이라는 함수 적용 즉 각 요소를 plus100의 인자로 전달
print(list(map(plus100,[i for i in range(1,6)])))
print('[람다함수 정의하여 사용하기]')
lambda_func = lambda arg : arg+100
print('value:{},type:{}'.format(lambda_func,type(lambda_func)))
print(list(map(lambda_func,[i for i in range(1,6)])))
print(list(map(lambda a:a+100,[i for i in range(1,6)])))#람다함수를 직접 인자로 전달
print('[람다표현식을 리스트의 요소로 사용하기]')
list_ = [lambda a,b : a+b,lambda  a,b:a-b,lambda a,b:a*b,lambda a,b:a/b]
print('value:{},type:{}'.format(list_[0],type(list_[0])))
print(list_[0](10,20))
print('{} + {} ={}'.format(10,20,list_[0](10,20)))
print('{} - {} ={}'.format(10,20,list_[1](10,20)))
print('{} * {} ={}'.format(10,20,list_[2](10,20)))
print('{} / {} ={}'.format(10,20,list_[3](10,20)))
print('[람다표현식을 딕셔너리의 값 요소로 사용하기]')
dict_ ={'+':lambda a,b:a+b ,'-':lambda a,b:a-b,'*':lambda a,b:a*b,'/':lambda a,b:a/b}
print(dict_['+'](10,20))
for key,value in dict_.items():
    print('{} {} {}={}'.format(10,key,20,value(10,20)))

print('[람다함수를 직접 호출하기]')
print((lambda a:a)('람다함수'))
#print((lambda  a : a*=2)(2))#SyntaxError: invalid syntax

#print((lambda a : a+b)(100))#NameError: name 'b' is not defined
b=100
print((lambda a : a+b)(100))#[o]
print('[매개변수에 초기값을 지정한 람다함수]')
lambda_ = lambda a,b=10 : a+b
print(lambda_(100))
print(lambda_(100,100))
print('[매개변수에 가변인수(위치 및 키워드)을 지정한 람다함수]')
lambda_ = lambda a,*args : a if args == tuple() else args
print(lambda_(100))
print(lambda_(100,200))
print(lambda_(100,*[100,200,300]))
lambda_ = lambda  a,*args,**kwargs : [a,args,kwargs]
print(lambda_(100))
print(lambda_(100,200,300))
print(lambda_(100,200,300,name='가길동',age=20))
#조건부 표현식(식1 if 조건 else 식2)을 람다 표현식에 사용하기
#즉 else문이 빠지면 안되고 elif가 포함되면 에러
#for문 사용할 수 없다
print((lambda a : a*2 if a%2==0 else a)(99))




