import math,sys
from decimal import Decimal

'''
파이썬은 부동 소수점 방식으로 실수를 표현하는데 
고정 소수점 방식보다 넓은 범위의 수를 나타낼 수 있어 
과학기술 계산에 
많이 이용되지만, 근삿값으로 표현한다
단,고정 소수점 방식보다 연산 속도가 느리다 
즉,0.1+0.2의 결과인 0.30000000000000004는 0.3을 표현한 근삿값이다
'''

a=0.1
b=0.2
print(a+b==0.3) #False

'''
실수를 근삿값으로 표현하면서 발생하는 문제를 
부동소수점 반올림 오차(Floating Point Rounding error)라고 한다. 
따라서 실수를 비교할 때는 연산한 값과 비교할 값의 차이를 구한 뒤 
sys.float_info.epsilon보다 작거나 같은지 판단해야 한다
'''
print("[부동 소수점 반올림 오차 해결 방법1] (epsilon)")
'''
2.220446049250313e-16(sys.float_info.epsilon)값을 
머신 엡실론(machine epsilon)
이라고 한다
연산한 값(a+b)과 비교할 값(0.3)의 차이가 머신 엡실론보다 
작거나 같다면 두 실수는 같은 값이라 할 수 있다.
'''
print(math.fabs(a+b -0.3)<=sys.float_info.epsilon)

#파이썬3.5이상부터는 두 실수가 같은지 판단할 때 math.isclose 함수를 사용
print("[부동 소수점 반올림 오차 해결 방법2] (isclose)")
print(math.isclose(a+b,0.3)) # True

print("[부동 소수점 반올림 오차 해결 방법3] (Decimal)")
#decimal 모듈의 Decimal로 고정 소수점으로 변환 -
# 고정 소수점은 부동소수점처럼 반올림 오차가 없다
print(Decimal("0.1")+Decimal("0.2")==Decimal("0.3"))
