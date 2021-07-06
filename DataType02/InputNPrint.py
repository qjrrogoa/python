'''
input()함수: 표준입력(키보드)으로 부터 사용자 입력을 받는 함수.이 함수가 실행되기 전까지
             Blocking상태가 된다. 즉 다음 라인의 코드가 실행이 안되고 멈춘다
             입력한 값은 모두 문자열<class 'str'>로 처리된다.


방법1]한번에 하나의 데이타만 입력받기
변수 = input()
변수 = input('안내 메시지')
'''
print("[input 함수]")
'''
print("나이를 입력하세요 : ",end="")
a = input()
print("a의 값 : {}, a의 타입 : {}".format(a,type(a)))
'''

''' 
방법2]한번에 여러 데이타를 입력받기
-input()함수에서 문자열 객체의  split()함수(구분자를 기준으로 분리하는 함수로 반환값은 리스트타입)를 호출하여
 여러 개의 변수에 저장(각 변수는 콤마로 구분)
 구분자 생략시 공백을 기준으로 분리한다.

변수1, 변수2,... = input().split() 
변수1, 변수2,... = input().split(구분자)
변수1, 변수2,... = input('안내 메시지').split()
변수1, 변수2,... = input('안내 메시지').split(구분자)
'''
'''
a=input("나이를 입력하세요 : ")
print("a의 값 : {}, a의 타입 : {}".format(a,type(a)))
'''

'''
#c= input("값을 여러개 입력하세요(콤마) : ").split(",")
#print("c의 값 : {}, c의 타입 : {}".format(c,type(c)))

print("[data 여러개 입력 받기 - 공백(디폴트) 구분자]")
a,b = input("공백을 기준으로 두개의 숫자를 입력하세요?").split()
print("a:{},b:{}".format(a,b))
c=int(a)+int(b)
print("두 숫자의 합 :",c)

print("[data 여러개 입력 받기 - 다른 구분자]")
a,b = input("콤마를 기준으로 두개의 숫자를 입력하세요?").split(",")
c=int(a)+int(b)
print("두 숫자의 합 :",c)

'''
'''
혹은 입력받은 값을 숫자(정수 혹은 실수)로 변경시 map함수를 이용하면 편리하다
map(함수,리스트 혹은 튜플)는 리스트의 요소를 첫번째 인자로 지정한 함수를 이용해서 
처리해주는 함수이다.
단,튜플일때는  원본 튜플을 변경하는 것이 아니라 새 튜플을 생성한다
변수1, 변수2,... = map(int 혹은 float, input().split())
변수1, 변수2,... = map(int 혹은 float, input().split(구분자))
변수1, 변수2,... = map(int 혹은 float, input('안내 메시지').split())
변수1, 변수2,... = map(int 혹은 float, input('안내 메시지').split(구분자))
'''
#m = map(int,input("두 개의 숫자를 입력하세요").split())
#print("m의 값 : {}, m의 타입 : {}".format(m,type(m)))
#print(dir(m))
a,b = map(int,input("두 개의 숫자를 입력하세요").split())
print("두 숫자의 합 : ",a+b)

'''
※ 콤마로 구분해서 여러개 값을 출력할 수 있다
print(값1, 값2, 값3,..[,sep='문자 또는 문자열'][,end='문자 또는 문자열'][,file=파일포인터)]
sep키워드 인수:콤마로 구분된 값을 여러 구분자로 결합하여 출력할 수 있다. (기본값은 공백)
end키워드 인수:출력시 줄바꿈 효과를 변경할 수 있다. (기본값은 \n)
file키워드 인수:출력 결과를 파일, 표준 에러처리로 보낼 수 있다.
'''
print("[print()함수]")
print("1. 여러개 동시에 출력하기 : 공백(디폴트)")
print(a,b,"공백")

print("2. 여러개 동시에 출력하기 : sep사용")
print(a,b,"sep키워드 사용",sep="▲")
print("2-1. 여러개 동시에 출력하기 : seq 사용 - 줄바꿈")
print(a,b,"sep키워드 사용",sep="\n")

print("3.여러개 동시에 출력하기 : end사용")
print(a,b,sep=",",end="")
print("입니다.")

print("4. 여러개 동시에 출력하기 : file 사용 - 표준 에러 출력")
import sys
print(a,b,file=sys.stderr)

print("5.여러개 동시에 출력하기 : file 사용 - 파일로 출력")
f = open("output.txt",'w')
print(a,b,sep='\n',file=f)
f.close()

