#{key:value}를 사용해서 딕셔너리 만들때는 키가 문자열인 경우에는 반드시
#'나 "로 키를 감싼다
#dict(key=value_를(생성자) 사용해서 딕셔너리 만들때는 키가 문자열인 경우
#'나 "로 키를 감싸면 안된다.
def pprint(obj):
    print("value",obj,",type",type(obj),'len:',len(obj),sep='')

print("[딕셔너리 생성 첫번째 : 빈 딕셔너리]")
#{}혹은 아래 dict()
a=dict() #혹은 a={}
pprint(a)

print("[딕셔너리 생성 두번째 {} 사용]")
#문자열은 반드시''나 ""로 감싸야 한다

a={'name':"가길동","age":20,"addr":"가산동",6:"6강의실"}
pprint(a)

#키값이 중복되는 경우 나중에 지정한 키값이 저장된다.
a={'name':"가길동","age":20,"addr":"가산동",6:"6강의실",'name':"나길동"}
pprint(a)


print("[딕셔너리 생성 세번째 : {} 사용]")
#키는 문자열뿐만 아니라 리스트와 딕셔너리를 제외한 모든 자료형이 키가 될 수 있다.
a={1:'one',(2,):'two',False:0,3.14:['파이','PI']}
pprint(a)
#키값으로 리스트와 딕셔너리는 사용할 수 없다.

print("[딕셔너리 생성 네번째 : dict()생성자 함수 사용]")
#dict(키 = 값) 함수 사용시 키는 '',""로 감싸면 에러
a=dict(name='가길동',age=20,addr='가산동')
pprint(a)

#a=dict(1='one') #[x]dict()함수 사용시 int/bool/float를 키로 사용불가
print('[딕셔너리 생성 다섯번째:dict([(),[],,,,]) 생성자 사용]')
a=dict([('name','최길동'),['age',20],('addr','부산'),('tel','010')])
pprint(a)

#튜플을 딕셔너리로 변환
a=dict((('name','최길동'),['age',20],('addr','부산'),('tel','010')))
pprint(a)

print('[딕셔너리 생성 여섯번째:dict(zip()) 생성자 함수 사용]')
#zip함수를 이용해서 dict만들 때 zip함수의 인자는 반드시 반복가능한 객체가 2개가 와야 한다.
#첫번째는 키가 되고 두번째는 벨류가 된다
#반복가능한 객체의 요소수가 동일하지 않으면, 적은 요소를 가진 객체를 기준으로
#딕셔너리가 만들어진다.
z=zip(['가','나','다'],['A','B','C'],[1,2,3])
print("value:{},type:{}".format(z,type(z)))
print(list(z))
#print(d)#{}
z=zip(('name','age','addr'),('다길동',30,'청담동'))
d=dict(z)
pprint(d)

z=zip(('name',),('다길동',30,'청담동'))
d=dict(z)
pprint(d)

f={3.14:['파이','PI'],1:'일',False:"거짓","과목":"파이썬"}
print(f[3.14])
print(f[1])
print(f[False])
print(f['과목'])
# print(f['name'])  #없는 키로 값 읽을 시 KeyError: 'name'
# get(키): 키값이 없는 경우 에러가 안나고 None반환
print(f.get(3.14))
print(f.get('name'))  #None
# get(키, '기본값'): 키가 없는 경우 기본값 반환
print(f.get('name', '키가 없는 경우'))

print('[딕셔너리에 값 할당하기]')
# 딕셔너리객체[키] = 값
# 만약 없는 키에 값을 할당시 새롭게 키와 값의 쌍이 추가된다
f[3.14] = ('파이',)
f[1] = '하나'
f['KOSMO'] = '한소인'
pprint(f)
