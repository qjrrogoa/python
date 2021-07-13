'''
매개변수의 순서:
1.고정인수 > 가변인수
2.위치가변인수(*) >키워드 가변인수(**)
3.고정인수 > 위치 가변인수 > 키워드 가변인수 > 매개변수 초기화
'''
print('[매개변수 초기값 설정하기]')
def args_init(arg1,arg2,arg3='디폴트값1',arg4='디폴트값2'):
    print(arg1,arg2,arg3,arg4,sep=' | ')

args_init(10,20)
args_init(10,20,30)
'''
def args_init2(arg1,arg2='기본값1',arg3):
    pass
'''
#args_init2(10,20)#SyntaxError: non-default argument follows default argument
help(print)#help함수로 print사용법 보기
help(map)
