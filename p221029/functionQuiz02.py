
## 덧셈 결과 출력하는 함수 정의하기
# 함수명 add , 매개변수 2개  리턴 값 없음.


## 함수 실행 결과 
'''
덧셈 결과 : 9 
덧셈 결과 : onetwo 
자료형 달라서 덧셈 불가능

        try:
            print(f'덧셈 결과 {p1+p2}')
        except:
            print('자료형 달라서 덧셈 불가능')

'''




## 함수정의 >> 
def add(p1, p2):
    try:
        print(f'덧셈 결과 {p1+p2}')
    except:
        print('자료형 달라서 덧셈 불가능')


## 호출 결과
add(5,4)
add('one','two')
add(1, 'one')


'''

def add(n1, n2):
    if type(n1) != type(n2):
        print('자료형 다르다 ')
        return
    print(n1+n2)

'''