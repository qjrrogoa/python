print("[set 표현식 첫 번째 - {}]")
print({i for i in 'HELLO'}) #{'H','E','L','O'}

print('[set 표현식 두 번째 - set{}]') #dict({}) 형태
print(set({i for i in 'HELLO'}))
print(set(i for i in 'HELLO'))

print("[set 표현식 세 번째 - 딕셔너리]")
a={'kor':90,'eng':80,'math':100}
print({key for key in a}) #a.keys()와 같다
print({key for key in a if key !='math'})
print({value for value in a.values()})


