print("[함수형식 1 - 매개변수 NO, 반환값 NO]")
def func1():
    print('='*30)
    print("1. NEW 2. CONTINUE 3. EXIT")
    print('='*30)
func1()

print("[함수형식 2 - 매개변수 NO, 반환값 YES]")
def func2():
    sum_ = 0
    for i in range(1,11):
        sum_ += i
    return sum_
#함수 호출
#방법1] 반환값 변수에 저장
sum_ = func2()
print("1부터 10까지 누적 합",sum_)

#방법2] 변수 미 사용 : 반환값 바로 출력
print(func2())

'''
    사용자로부터 국영수 점수를 입력받아
    평균을 구해서 학점을 반환하는 함수 정의
    예] 'A학점', 'B학점'...
'''

'''
def grage():
    subject = '국어','영어','수학'
    total = 0
    jumsu = [] # 빈 리스트
    for index in range(len(subject)):
        jumsu.append(input(subject[index]+"점수를 입력하세요 : "))
        total+=int(jumsu[index])

    avg = total / len(subject)
    print('평균 : %.2f' % avg)
    if avg >= 90:
        return 'A학점'
    elif avg >= 80:
        return 'B학점'
    elif avg >= 70:
        return 'C학점'
    elif avg >= 60:
        return 'D학점'
    else:
        return 'F학점'

print("당신의 학점은",grage())

'''
'''
    함수안에서 사용자로부터 숫자 두개와 산술연산자를 입력받는 함수로
    산술 결과는 함수 안에서 바로 출력하고
    산술 연산자 기호를 반환하는 함수를 정의해라
    그리고 함수를 호출하여 사용자가 입력한 연산자를 출력하여라
'''

def func2():
    a, b = map(int,input("숫자 두개를 입력하세요 : ").split())
    c = input("연산자를 입력하세요 : ")
    if c =='+':
        print(a + b)
        return c
    elif c=='-':
        print(a - b)
        return c
    elif c=='*':
        print(a * b)
        return c
    elif c=='/':
        print(a / b)
        return c
    else:
        return print("연산자를 다시 입력해주세요")

print(func2())