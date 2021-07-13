'''
인수의 갯수에에 따른 분류:
    고정인수-인수의 갯수가 정해진 인수
   가변인수-인수의 갯수가 정해지지 않고 가변적으로 변하는 인수
               함수정의시 매개변수앞에 *나 **를 붙이면 가변인수가 된다
        *는 위치인수를 가변인수로 사용할때
        **는 키워드인수를 가변인수로 사용할때
매개변수를 키워드로 사용하는지 여부에 따른 분류:
  위치인수 - 사용하지 않음
  키워드인수- 사용
'''
print('[고정인수를 사용한 함수]')
def fixed_args(age,tall,weight):
    print('나이:{},키:{},몸무게:{}'.format(age,tall,weight))
#함수 호출.인수의 위치 및 갯수 기억해야한다
fixed_args(30,190,60)
fixed_args(190,30,60)
#fixed_args(50,170)#TypeError: fixed_args() missing 1 required positional argument: 'weight'
age,tall,weight=[20,84,80]
print('나이:{},키:{},몸무게:{}'.format(age,tall,weight))
#인자로 리스트등을 전달할때 인자에 *를 붙이면 언패킹된다
fixed_args(*[20,84,80])#리스트가 언패킹이 되서 fixed_args(20,84,80)와 같다
print('[위치인수를 받는 가변인수를 사용한 함수]')
def variable_args(*args):#args는 가변인수이자 위치인수이다.args는 튜플로 생성된다
    print('value:{},type:{}'.format(args,type(args)))
    '''
    sum_ =0
    for i in args:
        sum_ += i
    print('인수가 {}개인 튜플의 합:{}'.format(len(args),sum_))
    '''
    print('인수가 {}개인 튜플의 합:{}'.format(len(args), sum(args)))


variable_args()#빈 튜플 ,()
variable_args(10,20)
variable_args(10,20,30,40,50)
variable_args(*[10,20,30,40,50])
print('[고정인수와 위치인수를 받은 함수 정의하기]')
#인수는 최소 1개를 전달해야하는 함수
def fixed_variable(arg,*args):#고정인수가 항상 가변인수보다 앞에 와야한다.그렇지 않으면 함수 호출시 에러
    print('고정인수:{},가변인수:{}'.format(arg,args))
    print('[가변인수의(튜플)의 모든 요소 출력]')
    for i in args:
        print(i)

fixed_variable(10)#고정인수 하나
fixed_variable(10,20,30)
fixed_variable(*[10,20,30])#위와 같다




