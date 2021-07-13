print('[고정인수를 받는 함수]')
def fixed_args(name,age,addr):
    print('이름:{},나이:{},주소:{}'.format(name,age,addr))
#함수 호출.인수 전달시 인수의 순서와 갯수 를 기억해서 함수를 호출해야 한다
fixed_args('가길동',20,'가산동')
fixed_args(*['가길동',20,'가산동'])
fixed_args(*{'age':40,'addr':"다산동",'name':'다길동'})#한번 언패킹이 일어나는데 ,딕션너리에 요소 순서대로 매개변수에 키값이 전달된다
fixed_args(**{'age':40,'addr':"다산동",'name':'다길동'})#두번의 언패킹이 일어나서 정확히 매개변수와 키값이 일치하는 값이 매개변수에 전달된다
                                                      #반드시 매개변수명과 딕셔너리의 키값은 일치해야 한다
fixed_args(addr="라산동",name="라길동",age=100)



#매개변수명을 키워드로 사용해서 값을 전달:키워드 인수라고 한다
#키워드는 ' 나 "로 감싸지 않은다
#키워드 인수로 값 전달. 이때 순서는 상관 없다
#키워드명과와 매개변수명은 일치 해야한다
fixed_args(age=20,addr='가산동',name='가길동')
'''
※ *위치 가변인수를 받는 매개변수는 튜플이된다
  **키워드 가변인수를 받은 매개변수는 딕셔너리가 된다
'''
print('[키워드 인수를 받는 가변인수를 사용한 함수 첫번째]')
#키워드 인수를 받는 가변 매개변수는 앞에 **를 붙인다
def variable_args(**args):
    print('value:{},type:{}'.format(args,type(args)))
    print('-------가변인수의 모든 요소 출력-----------')
    for key,value in args.items():
        print('key:{},value:{}'.format(key,value))
variable_args()#빈 딕셔너리.value:{},type:<class 'dict'>
#variable_args('코스모')#TypeError: variable_args() takes 0 positional arguments but 1 was given
variable_args(username='코스모')#키워드는 임의로(키워드명이 키가 됨) ,키워드 갯수에 제한이 없다(가변이기때문)
variable_args(username='하길동',password='1234',contact='01012345678')
variable_args(**{'name':'사길동','pass':'9999','tel':'010-5555-7777'})

print('[키워드 인수를 받는 가변인수를 사용한 함수 두번째]')
def variable_args2(**kwargs):
    # in으로 딕셔너리 안에 특정 키가 있는지 확인
    if 'name' in kwargs:
        print('이름:',kwargs['name'])
    if 'addr' in kwargs:
        print('주소:', kwargs['addr'])

variable_args2(username='하길동',password='1234',contact='01012345678')
variable_args2(name='하길동',password='1234',addr='하산동')
#고정인수가 항상 가변인수보다 앞에 와야한다.그렇지 않으면 함수 호출시 에러
print('[고정인수와 키워드 인수를 받는 가변인수를 함께 사용하기]')
def fixed_variables(arg,**kwargs):
    print('고정인수:{},가변인수:{}'.format(arg,kwargs))
    print('-------가변인수의 모든 요소 출력-----------')
    for key, value in kwargs.items():
        print('key:{},value:{}'.format(key, value))
#fixed_variables()#TypeError: fixed_variables() missing 1 required positional argument: 'arg'
fixed_variables(10)
fixed_variables('파이썬',subject='파이썬',location='가산',institue='코스모')
fixed_variables('자바',**{'subject': '자바', 'location': '가산'})



