print("[리스트의 주요 메소드]")

print("1. index(요소) : 튜플 요소의 인덱스 반환, count(요소) : 요소의 빈도수 반환")
g=("가","나","다","라","나","마","나")
print("'나'의 인덱스 :",g.index('나'))
#print("'바'의 인덱스 :",g.index('바')) #ValueError: '바' is not in list
if '바' in g:
    print("'바'의 인덱스 :", g.index('바'))
print("'나'의 빈도 수 :",g.count('나'))


print("[리스트의 산술 연산]")# +와 *만 가능
x=[1,2,3]
y=['가','나','다']
print(x+y)
# x.extend(y)
print(y*3)
print(x*0)#[]리스트에 0이나 음수를 곱

z=(1,2,3,)
print(4 not in z)
print(1 in z)