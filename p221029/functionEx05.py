# 리턴값


# 함수 정의
def div( n1, n2 ):
    result1 = n1 // n2 # 슬래시 2개쓰면 정수형태로만 나옵니다(내림)
    #     result1 = n1 // n2 
    result2 = n1 % n2
    result3 = n1 //n2
    return result1 , result2, result3
#보통함수를위한 별도의 파일을 따로 만들어두고. 그 파일안의 
# 함수를 호출해서 사용하는게 보통입니다.
#우리는 상황이있어서 동일 파일내에서, 순차적으로 작성해서 쓸 뿐입니다.

#g함수 호출합니다. 

divResult  = div( 5,3)
print('div(5,3)의 결과 ?  >> ', divResult )
print('div(5,3)의 결과 ?  >> ', type(divResult) )


tup = {1,2,1}
print(tup)

# 파이선의 함수는 return 에 두개이상 값이 올수있다 ( 0 ) 
# 파이썬함수는 두개이상의 값을 반환한다 ( X )
#  튜플이라는 단위, 한덩어리로 묶여서  반환되는 값은 하나이다 
# 튜플자료형 하나