
# 정수 2개 입력시 두수의 누적합 출력한다 
def accumulator(n1, n2):
    result =0
    # step = 1 
    # for i in range(n1,n2+1):
    #     result = result + i
    # if(n1>n2):
    #     result =0
    #     for i in range(n2,n1+1):
    #         result =result +i 
    result =   sum(range(n1,n2+1) )  if n1 <=n2 else sum(range(n2,n1+1))
    ## 조건 연산자  true 인경우 왼 , FALSE인경우 오 
    # T일때 if 조건씩 else F 일때 

    result = sum(range(n1,n2+1)) if n1 <= n2 else sum(range(n2,n1+1))

    return result
'''
#함수
def accumulator(n1,n2): 
    #주의 sum 은 내장 함수가 있으므로 피합니다. 
    # add 를 둡시다.    add = sum(iterable)
    # 큰 작 비교를 합니다. 
    if n1 > n2:
        max , min = n1 , n2
    else:
        max, min = n2 , n1
    add = sum(range(min, max +1 ))
    print('누적합>> ' , add )
    # 조건 연산자 
    add = sum(range(n1,n2+1)) if n1 > n2 else sum(range(n2,n1+1))

    max, min  = n1, n2 if n1 > n2  else n2, n1  # Too many Values 에러가남!
    #그래서 튜플, 리스트로 하나로 묶어서 보내주어야한다
    max,min = (n1,n2) if n1> n2 else (n2, n1 )  


'''


print('문제1',  accumulator(1,10))
print('문제1',  accumulator(10,1))


#문제 4 리스트 인수로 positive 함수 호출시 양수값만 리턴하는 함수 

'''
호출 : 

positiveValue = positive( [1,-2,3,-4,5])

print(positiveValue)


'''
def positive( listArg):
    result = []
    for i in listArg:
        if i>0:
            result.append(i)

    return result

positiveValue = positive( [1,-2,3,-4,5])

print(positiveValue)
'''
리스트에서 하나씩 빼서 검사 
반복문! 
양수 ? 기니 마니? 

함수 정의 
def positive( list ):
    


'''




print('=================================')
n1 = 3
n2=5
print(' 조건 연산자 참고 ')
max,min = (n1,n2) if n1> n2 else (n2, n1 )  
print( max, '----', min)