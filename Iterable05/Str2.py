print("[문자열 관련 주요 메소드]")
def pprint(value):
    print("value : {} \ntype : {}".format(value,type(value)))
print("1. join() 리스트(이터러블객체)를 문자열로")
# 단, 리스트의 모든 요소는 문자열이어야 한다. 리스트 요소 중 하나라도 숫자인 경우 에러 발생
# 이런 경우 map함수를 보통 같이 적용한다.
a=["한라산","설악산","대둔산","덕유산"]
b="▲".join(a)
pprint(b)

a.append(2021)
print(a) #['한라산', '설악산', '대둔산', '덕유산', 2021]
#b="▲".join(a) #TypeError: sequence item 4: expected str instance, int found
b="▲".join(map(str,a))
pprint(b)

print("2. split() : 특정 구분자로 split해서 리스트를 반환(디톨트가 공백)")
c=b.split("▲")
pprint(c)

#구분자가 없는 경우 문자열 전체가 리스트의 하나의 요소로 생성된다.
d=b.split()#공백으로 split
pprint(d) # 요소가 하나인 리스트로 변경

print("3. replace() : 문자열 변경")
e="Hello World"
print(e.replace('World',"Python"))

print("4. lower() : 소문자로 변경")
print(e.lower())

print("5. upper() : 대문자로 변경")
print(e.upper())

print("6. lstrip([문자열]) : 왼쪽의 공백제거")
f = "          Hello    World      "
print('{}{}{}'.format('X',f.lstrip(),"Y"))
print('{}{}{}'.format('X',f.lstrip("          He"),"Y"))

print("7. rstrip([문자열]) : 오른쪽의 공백제거")
print('{}{}{}'.format('X',f.rstrip(),"Y"))
print('{}{}{}'.format('X',f.rstrip().rstrip("ld"),"Y"))

print("8. strip([문자열]) : 양쪽의 공백제거")
print('{}{}{}'.format('X',f.rstrip().lstrip(),"Y"))
print('{}{}{}'.format('X',f.strip(),"Y"))

print("9. zfill(자리폭) : 0으로 자리수 채우기")
print("9".zfill(2))
print("3.14".zfill(6))
#문자열의 길이보다 지정된 자리 폭의 길이가 작거나 같으면 아무것도 채우지 않는다.
print("PYTHON".zfill(1))

g="Hello ! He is a good"
print("10. find()/rfind():문자열 찾기(찾은 문자열의 인덱스 반환)")
#찾은 문자열이 없는 경우 -1 반환
print(g.find("He"))
print(g.rfind("He"))
print(g.find("he"))

print("11. index()/rindex():문자열 찾기(찾은 문자열의 인덱스 반환)")
#찾은 문자열이 없는 경우 에러
print(g.index("He"))
print(g.rindex("He"))
#print(g.index("he")) 에러

print("12. count() : 찾은 문자열의 갯수 반환")
print(g.count("He"))
print(g.count("he"))

