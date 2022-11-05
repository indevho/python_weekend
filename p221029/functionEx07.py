'''
변수 종류 

전역변수
지역변수


num =5


'''

num =5 

def increment():
    #num = 100 지역 변수 
    global num # 이 num 전역변수 이다 선언
    # global declaration 이라고 한다..
    num = num + 1 
    # 이 num 이 전역변수에요 . 

    print('함수내에서 num>> ', num)
def incrementglobal():
    global num
    num = num + 1 
    print('함수내에서 num>> ', num)


print('before num : ', num)


increment()# 에러가 남
# 함수 내에 num 선언 후에는안남

#UnboundLocalError: 
#local variable 'num' referenced before assignment

print('after num : ', num)


# 매개변수 입장하는 순간 "지역변수:"
# 함수끝나는순간 메모리에서 clear 된다






