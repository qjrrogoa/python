i=0
while i <100000000:
    i+=1
    print("[i가 {}일때]".format(i))
    print("continue이전 출력문")
    if i%2==0:
        continue
    print("continue이후 출력문")
    print("break이전 출력문")
    if i==3:
        break
    print("break이후 출력문")