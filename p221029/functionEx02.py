#함수정의
# 기능 정수 1 증가하여 출력하기 
# 영어, 동사형태 주로 쓴다.

# 정의 하는 놈 따로 
def add(n1, n2):
    result = n1+ n2
    return result
    print('n1+n2')
# return 아래 코드작성은- 잘못 작성한 코드이다. 
# RETURN 만나면서 어차피 해당함수의 실행은 끝 난다. 


addResult = add(2,6)
print('ㅁadd호출결과>>',addResult)
#not defined . 위치가 중요..!
# 실행 아무리 해도, 그 정의는 , 실행  "이전" 에 확인이 되어야만 한다



# 함수 호출 ---------------------
# print(add(1,2))
# add(1,2) 는 return 뒤에있는 하나의 값으로 대치된다
# positional arg : 아예 함수에서 파라미터값에 박아넣은 arg
# non-keyword arg :  = " "  가 주어지지 않은 일반 arg
# keyword arg :  = " " 가 주어진 def값을 알고있는 arg 
# arbitrary arg  -  greet(*names)

# def greet(*names):
#     for i in names:
#         print(f'hello{i}')

# greet('aa','bb','cc')