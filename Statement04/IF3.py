kor,eng,math = 99,80,96
avg = (kor+eng+math)/3
if avg >= 90:
    print("A학점")
elif avg >= 80:
    print("B학점")
elif avg >= 70:
    print("C학점")
elif avg >= 60:
    print("D학점")
else :
    print("F학점")

'''
    사용자로 부터 한 문자를 입력받아 숫자이면 "숫자"
    알파벳이면 "알파벳"
    숫자도 알파벳도 아니면 "기타"를 출력하여라.
    if ~ elif ~ else 사용
'''
word = input("한 문자를 입력하세요 : ")
if '0' <= word <= '9':
    print("숫자")
elif 'a' <= word <= 'z' or 'A' <= word <= 'Z':
    print("알파벳")
else :
    print("기타")


#문] (종합) 세 숫자 중 최대 값을 구하는
# 로직을 작성하자

num1,num2,num3=199,204,19
max = num1
if max < num2 :
    max = num2
if max < num3 :
    max = num3
print("최대값",max)