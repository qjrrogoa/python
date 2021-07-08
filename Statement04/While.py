#1부터 10까지 누적합:while문 사용
sum = 0
i = 1 # 초기식
while i <= 10: #반복 조건
    sum+=i #실행문
    i+=1 #증감식
print("1부터 10까지의 누적 합",sum,sep=":")

'''
문]1부터 1000까지 숫자중 3의 배수기어나 5의 배수인 숫자의 합을 구해라
단, 3과5의 공배수인 경우 제외
'''
sum=0;
i=1
while i <= 1000:
    if (i % 3 == 0 or i % 5 == 0) and i % 15 != 0:
        sum += i  # 실행문
    i += 1  # 증감식
print(sum)

'''
import random
i=1
while 1 != 5:
    i = random.randint(1,10) #1부터 10까지 난수 발생
    print("i는",i)
'''

i=1
k=1
while i<5:
    while k<5:
        if k ==i:
            print("1",end=" ")
        else:
            print("0 ",end=" ")
        k+=1
    k=1
    i+=1
    print()

k=1
while k<=5:
    j=1
    while k >= j:
        print("*",end=" ")
        j+=1
    print()
    k+=1

i=1
while i<=9:
    k = 2
    while k<=9:
        print("{} * {} = {}".format(k,i,i*k),end="     ")
        k+=1
    print()
    i+=1