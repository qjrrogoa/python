'''
순서가 있는 자료형(시퀀스 객체):str,list,tuple,range
공통 기능
1. (not) in 연산자로 요소(객체) 존재 파악
2. 인덱싱([인덱스]) 및 슬라이싱([시작인덱스 : 끝인덱스])
3. + 나 * 연산자로 시퀀스객체를 연결(+)하거나 같은 시퀀스객체를 배수(*)로 늘릴 수 있다
   단,range객체는 list로 변환후 +,*를 적용하자
   그리고 *연산자 사용시 0이나 음수를 곱하면 빈 객체가 된다
4. len(시퀀스객체)함수는 저장된 요소의 갯수 반환
'''
print('[빈 문자열 만들기]')
a=''#"",'''''',"""""",str()
#len(반복가능한 객체)는 모든 반복 가능한 객체의 요소수를 반환
print('value:{},len:{},type:{}'.format(a,len(a),type(a)))

print('[NOT 빈 문자열 만들기]')
a='PYTHON'
print('value:{},len:{},type:{}'.format(a,len(a),type(a)))

#순서가 있는 자료형(str,list,tuple,range)들은 각 요소에 인덱스로 접근 가능
#시퀀스객체[인덱스]
#인덱스는 양수(인덱스는 0부터 시작하고 왼쪽기준) 혹은 음수(인덱스는 -1부터시작하고 오른쪽 기준)
'''
print('[인덱스로 요소에 접근하기]')
#index=(list(map(int,input("추출할 문자의 입력 : (단, 최대값은 {})".format(len(a)-1))))[0]
index = int(input("추출한 문자의 인덱스를 입력 : (단 최대값은 {})".format(len(a)-1)))
print("양수 인덱스(왼쪽부터 인덱싱) : ",a[index])
print("음 인덱스(오른쪽부터 인덱싱) : ",a[-index])
print(a[-1])
#print(a[len(a)])#IndexError: string index out of range
'''

'''
print("[문자열에 for문 적용하기]")
index = 0
for element in a:
    print("인덱스 : {},요소 : {}".format(index,element))
    index+=1
'''

# enumerate(순서가 있는 자료형): 리스트, 튜플, 문자열객체,range객체의 요소의 순서(인덱스)와 요소를
# 튜플로 묶어서 enumerate 객체(반복가능한 객체)로 반환
# ※ 보통 enumerate 함수는 for문과 함께 자주 사용된다.
for index, element in enumerate(a): #튜플인 각 요소를 구조분해(언팩킹)로 각 변수에 저장
    print("인덱스 : {},요소 : {}".format(index,element))

print("[시퀀스 객체[인덱스]=새로운 요소로 변경하기]")
#a[0] = 'B' #TypeError: 'str' object does not support item assignment

#문자열의 값을 변경하려면 리스트로 변환 후 변경해야 한다.
#1. 먼저 문자열을 리스트로 변환한다.
a=list(a)
print("value : {}, type : {}".format(a,type(a)))
#2. 특정 인덱스의 문자열을 변경한다.
a[0] = 'B'
print(a)
#3.리스트를 다시 str로 변경
#아래처럼 sr함수로 문자열로 변환하면 리스트형태가 그대로 문자열로 변경된다.
#a= str(a)

print("value : {}, type : {}".format(a,type(a)))
#4. Join()함수를 사용하거나 아래처럼 리스트의 각 요소를 문자열에 누적하여 변경된 문자열을 만든다.
b = ''.join(a)
print("value : {}, type : {} (Join함수 사용)".format(b,type(b)))

#4-1
b=""
for temp in a:
    b+=str(temp)
print("value : {}, type : {} (Join함수 미 사용)".format(b,type(b)))

#슬라이싱 : 인덱스를 사용해서 특정 범위의 요소들을 꺼내올 수 있다.(시퀀스 객체이 경우)
print("[문자열 slicing]")
d="ABCDEFG"

#[시작인덱스 : 끝 인덱스] - 시작인덱스부터 끝 인덱스 -1까지
print(d[1:3]) # BC
print(d[1:-3]) # 1부터 -4까지 나옴 BCD
#[:끝인덱스] - 처음부터 끝 인덱스 -1까지
print(d[:4]) # ABCD

#[시작인덱스:] - 시작인덱스부터 끝까지
print(d[-len(d):]) # ABCDEFG

#[:] - 모든 요소 슬라이싱
print(d[:]) #ABCDEFG

#in (not in)  연산자 : 모든 시퀀스 객체에 공통으로 적용될수 있는 연산자
#                     객체안의 특정 요소의 존재여부를 파악할 수 있는 연산자
#찾을객체 in 반복가능한 시퀀스객체

#in (not in) 연산자 : 모든 시퀀스 객체에 공통으로 적용될 수 있는 연산자
#                    객체안의 특정 요소의 존재여부를 파악할 수 있는 연산자
# 찾을 객체 in 반복가능한 시퀀스 객체
e="JAVA"
print('A' in e)
print("A" not in e)
print("AVA" in e)
print("Ava" in e)

while True:
    email = input("이메일 주소를 입력하세요?")
    if "@" not in email:
        print("이메일 형식이 아닙니다.")
    else:
        break





