#pycharm인 경우 File->Settings->Editor->File Encodings인코딩 설정
#변경시 아래 인코딩 지정 불 필요
#coding:utf-8

#변수 선언 방법1] 변수명 = 데이터
a=10
print(a,type(a),sep="\n")#type(변수):자료형 반환 <class 'int'>

#변수 선언 방법2] 변수명1, 변수명2, 변수명3,.. = 반복 가능한 객체(이터레이터)
#이터레이터의 요소를 여러 변수에 나눠 담는것을 언패킹(unpacking) 또는 구조분혀(destructuring)라고 한다.
#변수명1, 변수명2, 변수명3 = 데이터1, 데이터2, 데이터3 혹은 (데이터1, 데이터2, 데이터3)
#특히 대입문에서는 패킹과 언패킹을 수행할 때 괄호를 생략하는 경우가 많다.
a,b,c='파이썬','10',20 #a,b,c=('파이썬','10',20)
print("a의 값 : %s a의 자료형:%s" % (a,type(a)))
print("b의 값 : {} b의 자료형 : {}".format(b,type(b)))
print("c의 값 :",c,"c의 자료형 :",type(c))

#변수 선언 방법 3] 변수명 = 반복가능한 객체(이터레이터)
#여러 개의 데이터를 이터레이터를 이용해 하나의 변수에 묶어 담는 것을 패킹(packing)
#변수명 = 데이터1, 데이터2, 데이터3 혹은 (데이터1, 데이터2, 데이터3)
d=10,'20','파이썬' # int,str,str객체를 튜플로 묶어서(패킹) 변수 d에 저장
print("d의 값 : {} d의 자료형 : {}".format(d,type(d)))

#변수 선언 방법 4] 변수명1 = None
z=None
print("z의 값 : {} z의 자료형 : {}".format(z,type(z)))
x,y=10,20
print("x = {} y= {}".format(x,y))
print('[x와 y값 치환]')
x,y=20,10
print("x = {} y= {}".format(x,y))

#변수 삭제
del(x) #혹은 del x
print(x)
#NameError: name 'x' is not defined
