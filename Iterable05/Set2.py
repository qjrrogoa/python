print('[집합의 주요 메소드]')
a={1,2,3,4}
b={3,4,5,6}

print('1. 합집합')
print(a | b)
print(set.union(a,b))
print(a) # in-place방식이 아님. a가 변하지 않는다
# a.update(b) # in-place방식 a가 변한다.
# print(a)

print('2. 교집합')
print(a & b)
print(set.intersection(a,b))
#a.intersection_update(b) # in-place방식 a가 변한다.
#print(a)

print("3. 차집합")
print(a - b)
print(set.difference(a,b))
#a.difference_update(b)
#print(a)

print("4. 대칭차집합")
print(a ^ b)
print(set.symmetric_difference(a,b))

print("5. add(요소)")
a.add(5)
print(a)

print('6. remove(요소)')
a.remove(3)
#a.remove(3) # 에러
print(a)

print('7. discard(요소)')
a.discard(2)
a.discard(2) #노에러
print(a)

print('8.clear()')
a.clear()
print(a) #set()

import copy
print('9.copy()')
a={1,2,3,4}
c=a.copy() #shallow copy : 주소 복사
print('a의 주소 : {}, c의 주소 : {}'.format(id(a),id(c)))

print('10. len()')
print(len(a))
#in (not in) 연산자 : 집합에 적용시 요소의 존재여부를 파악할 수 있다.
print('[집합에 in 및 not in 연산자 적용]')
a={'가','나','파이썬','자바'}
print('다' in a)
print('파이썬' in a)
print(a) # 순서가 없기때문에 출력시 순서없이 출력된다 실행시마다 다르다
a={2,5,94,3,997}
for element in a:
    print(element)