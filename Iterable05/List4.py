print('[리스트와 함께 쓰는 빌트인 함수]')
'''
min(반복가능한 객체(iterable)) : 요소중 최소값 반환
max(반복가능한 객체(iterable)): 요소중 최대값 반환
sum(반복가능한 객체(iterable)): 요소의 총합 반환
※위 함수들을 사용할때 반복가능한 객체의 요소들은 반드시 숫자 나 bool값이어야한다
map(함수, 반복가능한객체):
반복 가능한 객체의 요소를 첫번째 인자로 지정된 함수로 처리한 뒤 
map객체(이터레이터)를 반환
예) list(map(str, [1, 2]))는 ['1', '2']반환
'''
a=[10,5,15,50,True,False,-5,5]
print("[요소중 최대값 구하기 - 방법1]")
max_ = a[0]
for i in a[1:]:
    if i > max_:
        max_ = i
print("최대값 :",max_)

print("[요소중 최대값 구하기 - 방법2]")
a.sort(reverse=True)
print("최대값 :",a[0])

print("[요소중 최대값 구하기 - 방법3]")
print("최대값 :",max(a))

print("[리스트 요소의 합]")
print(sum(a))

b=[True,100,5,"가"]
#print(sum(b)) #에러

c=[3.14,5.99,8.88,1.24]
print("[리스트의 모든 요소를 정수로 변환하기]")

d=[]
for i in range(len(c)): #리스트의 요소 수만큼 반복하고 i를 인덱스로 사용
    d.append(int(c[i]))
print(d)

print("---map함수 미 사용 : 리스트 축약 사용---")
e = [int(i) for i in c]
print(e)

print("---map함수 사용---")
f = list(map(int,c))
print(f)

#세개의 숫자를 공백을 기준으로 input() 함수로 입력받고 각각의 입력받은 값을
# 공백을 기준으로 split(구분자)한다. 그리고 각 요소를 int로 변환하고 list로 만들어
#언패킹을 이용해서 세개의 변수에 저장


x,y,z=list(map(int,input("세 개의 숫자를 입력하세요 : ").split()))
print(x+y+z)
