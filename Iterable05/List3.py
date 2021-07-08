print('[리스트 표현식(축약,내포) 미 사용]')
a=[]
for i in range(5):
    a.append(i)
print(a)

print("[리스트 표현식(축약,내포) 사용 첫번째]")
#순서 : range(5) -> for문 안의 i -> for문 앞의 식 : i
#설명 : 숫자 0부터 4까지 생성(range(5))하여 for문 안의 i에 담고 그 i를 이용해서 식을 만들고
#그 식에 따라 리스트의 요소가 하나씩 생성된다
a=[i for i in range(5)]
print(a)

a=[i+2 for i in range(5)]
print(a)

a=[i > 1 for i in range(5)]
print(a)

print("[리스트 표현식(축약,내포) 사용 두번째]")

a=list(i+2 for i in range(5))
print(a)

a=list(i > 1 for i in range(5))
print(a)

#순서 : range(5) -> for문 안의 i -> for문 다음의 if문 -> if문이 참인 경우 식이 실행되서
# 요소가 하나 만들어진다
# 설명 : 숫자 0부터 9까지 생성하여 i에 저장하고 그 i가 2의 배수이면 for문 앞의
# 식이 실행되서 요소가 만들어진다
a=[i for i in range(10) if i % 2==0]
print(a)

a=[i * k for i in range(2,10) for k in range(1,10)]
print(a)
#위 리스트 표현식은 아래와 같다
b=[]
for i in range(2,10):
    for k in range(1,10):
        b.append(i*k)
print(b)

a=[i * k for i in range(2,10) if i==9 for k in range(1,10) if k==9]
print(a)
#위 리스트 표현식
c=[]
for i in range(2,10):
    if(i==9):
        for k in range(1,10):
            if(k==9):
                c.append(i*k)
print(c)