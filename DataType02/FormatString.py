'''
format string:출력형식을 지정하기 위한 형식 문자열

형식1] "형식문자열" %값  형식
     % 앞 부분은 포맷 문자열이고, % 뒤는 실제 대입할 값이다.
     이때 % 를 포맷팅 연산자(Formatting Operator)라 부른다.
     만약 % 뒤의 값이 복수 개이면 튜플로 묶어주어야 한다.

     예]
     name ='이름은 %s입니다' % '김길동'
     print(name)
     person = '이름:%s,나이:%d' % ('김길동',20)
     print(person)
     예 에서 %s나 %d등을 변환 지시자(Conversion Specifier)라고 한다
     주요 변환 지시어
      %d 또는 %i:정수값 출력시
      %f 또는 %F:실수값 출력시
      %c:한 문자 출력시
      %o 또는 %O:8진수 출력시
      %x 또는 %X:16진수 출력시
      %s:문자열 혹은 파이썬 객체를 str()을 사용하여 변환한 경우
      %r:문자열 혹은 파이썬 객체를 repr()을 사용하여 변환한 경우
      %%: %리터럴을 의미
형식2] "형식문자열".format(인자들)
        형식문자열 내의 변환 지시자의 형식은 {숫자}, {이름} 이다
             ※ 숫자 사용시 숫자는 0부터 시작 그렇지 않으면 아래 에러 발생
       IndexError: tuple index out of range
    예]
     name ='이름은 {0}이고 나이는 {1}살입니다'.format('김길동',20)
     print(name)
     person = '이름:{name},나이:{age}'.format(name='김길동',age=20)
     print(person)

'''
kor=99;eng=80;math=96
avg =(kor+eng+math)/3

print("[형식 문자열 미 사용시]")
print("국어:"+str(kor)+" 영어:"+str(eng)+" 수학:"+str(math)+ " 평균:"+str(avg))

print("[형식 문자열 사용시 - 포맷팅 연산자(%s)]")
print("국어:%d 영어:%d 수학:%d 평균:%f"% (kor,eng,math,avg))

print("[형식 문자열 사용시 - str객체의 format()함수 : 숫자 인덱스 사용]")
print("국어:{0} 영어:{1} 수학:{2} 평균:{3}".format(kor,eng,math,avg))

print("[형식 문자열 사용시 - str객체의 format()함수 : {}]")
print("국어:{} 영어:{} 수학:{} 평균:{}".format(kor,eng,math,avg))

print("[형식 문자열 사용시 - str객체의 format()함수 : 키워드 인수]")
print("국어:{kor} 영어:{eng} 수학:{math} 평균:{average}".format(kor=kor,eng=eng,math=math,average=avg))

#형식 문자열 쓰는 곳에서 특수문자(이스케이프문자) 사용 가능
print("[형식 문자열에 이스케이프 문자 혼용하기]")
print("국어:%d\t 영어:%d\t 수학:%d\t\n평균:%f"% (kor,eng,math,avg))

'''
   형식문자열에서 데이타 출력시 자릿수 지정
   %숫자format-string
   예]
   %4c : 한문자를 출력하는 데 전체 자리수는 4
   %5d: 정수 숫자를 출력하는 데 전체 자리수는 5
   %6.2f%:실수를 출력하는데
          소수점 둘째짜리까지만 출력하고
          전체 자리수는 6(소수점 포함)


   자릿수 지정시 값을 오른쪽부터 채운다
   -를 붙이면 왼쪽부터 채운다
   예]
   print("%4d" % 12);
   _ _ 12
   print("%-4d" % 12);
   12_ _
'''

print("[출력 자리수 미 지정]")
print("국어:%d 영어:%d 수학:%d 평균:%f"% (kor,eng,math,avg))

print("[출력 자리수 지정(양수)]")
print("국어:%4d 영어:%4d 수학:%4d 평균:%7.2f"% (kor,eng,math,avg))

print("[출력 자리수 지정(음수)]")
print("국어:%-4d 영어:%-4d 수학:%-4d 평균:%.2f"% (kor,eng,math,avg))


