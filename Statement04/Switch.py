'''
파이썬에는 switch문이 없다
딕셔너리와 사용자 정의 함수를 이용해서 switch문 효과를 낼 수 있다.
'''

kor,eng,math = 90,60,95
avg = (kor+eng+math)//30

#학점을 반환하는 함수 : switch
'''
def switch(key):
    #문자열 반환
    return {10:"A 학점",
            9:"A 학점",
            8:"B 학점",
            7:"C 학점",
            6:"D 학점"}.get(key,"F학점")

print("평균 : {}, 학점 : {}".format(avg,switch(avg)))
'''
def switch(key):
    #함수 반환
    return{
        10:lambda : print("A학점"),
        9:lambda : print("A학점"),
        8:lambda : print("B학점"),
        7:lambda : print("C학점"),
        6:lambda : print("D학점"),
        5:lambda : print("F학점"),
        4:lambda : print("F학점"),
        3:lambda : print("F학점"),
        2:lambda : print("F학점"),
        1:lambda : print("F학점"),
        0:lambda : print("F학점"),
    }[key]

f=switch(avg)
f()
switch(avg)() # f = switch(avg);f() 이 두 명령어를 하나의 명령어로!
print("value : {}, type : {}".format(f,type(f)))
#value : <function switch.<locals>.<lambda> at 0x000002E59863F280>, type : <class 'function'>
