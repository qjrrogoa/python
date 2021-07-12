#in (not in) 연산자 : 딕셔너리 적용시 딕셔너리에 키의 존재여부를 파악할 수  있다.
print("[딕셔너리에 in 및 not in연산자 적용하기]")
a=dict(name='홍길동',age=20,addr='가산동')
print('tall' in a)
print('tall' not in a)
print('name' in a)
print('name 키 존재 'if a.get('name')!=None else 'name키 없음')

print("[for문 사용 첫번째 - for 변수 in 딕셔너리 객체 : ]")
for key in a:
    value = a.get(key)
    print("key : {}, value:{}".format(key,value))

print("[for문 사용 두번째 - for 변수 in 딕셔너리 객체.items():]")
for key, value in a.items():
    print("key : {}, value : {}".format(key,value))

'''
for반복문으로 값을 찾아서 딕셔너리 요소 삭제하면 에러가 발생
즉 Iterating하는 동안 요소를 삭제하면 크기가 변하기 때문
'''

key_ = None;
for key,value in a.items():
    if value=="홍길동":
        key_=key
del a[key_]
print(a)

'''
{키:값  for 키[, 값 ] 혹은 [키,]값    in 딕션너리.items() }
{키:값  for 키[, 값] 혹은 [키,]값   in 딕션너리.items() if 조건식}

dict({키:값  for 키[, 값 ] 혹은 [키,]값  in 딕션너리.items()})
dict({키:값  for 키[, 값 ] 혹은 [키,]값  in 딕션너리.items() if 조건식})
딕션너리 표현식으로
특정 값을 기준으로 딕션너리를 다시 생성하는 방식으로 삭제 효과를 구현할 수 있다
'''
keys = ['A','B','C','D']
print("[딕셔너리 표현식 첫번째 - {} : 리스트로 생성") #리스트 요소를 키로 사용
#dict.fromkeys()사용
a=dict.fromkeys(keys,"PYTHON")
print(a)

#표현식 사용
b = {key:"PYTHON" for key in keys}
print("{}, type : {}".format(b, type(b)))

print("[딕셔너리 표현식 두 번째 - dict({}) : 리스트로 생성]")
c = dict({key:"PYTHON"+key for key in keys})
print("{}, type : {}".format(c, type(c)))

print("[딕셔너리 표현식 세 번째 - keys() : 기존 딕셔너리로 생성]")
d={key : len(key) for key in a.keys()}
print(d)

print("[딕셔너리 표현식 세 번째 - values() : 기존 딕셔너리로 생성]")
e={value : value for value in a.values()}
print(e)

print("[딕셔너리 표현식 세 번째 - items() : 기존 딕셔너리로 생성]")
f={value:key for key,value in a.items()}#키와 벨류 바꾸기
print(f)

f={'name':"가길동",'tel':'010','addr':'가산동'}
g={value : key for key,value in f.items() if key != 'name'}
print(g)

