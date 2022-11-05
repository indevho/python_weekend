'''
[튜플]
여러 데이터를 묶어서 단일한 이름으로 관리한다 
type :  tuple 
type 000 is tuple 

요소의 변경 (   추가,  삭제 , 수정(대치,대입 ) ) 이 불가능하다
그만큼 처음 선언 할때가 중요

단일값 추출: 인덱싱
'연속된' 여러값 추출 : 슬라이싱 
은 가능 ( why  : 복사의 개념이지, 원본을 건드리지않기때문 )

======================================
'''


lt =  [2,4,6]
tu = (1,3,5)
# 타입확인
print('리스트변수 lt 의 자료형>>',type(lt) is list)
print('리스트변수 tu 의 자료형>>',type(tu) is tuple)


# 인덱싱
print('첫번째요소 추출 >> ',lt[0])
print('마지막요소 추출 >> ',lt[-1])
print('첫번째요소 추출 >> ',tu[0])
print('마지막요소 추출 >> ',tu[-1])

#슬라이싱 ( 리스트에서는 리스트, 튜플에서 튜플이 나온다)
print('두번재에서 마지막까지 추출 >> ',lt[1:])
print('두번재에서 마지막까지 추출 >> ',tu[1:])

#에러확인 
# TypeError: 'tuple' object does not support item assignment
# 당신이 assign 이라는 행위를 시도하지만, 이 type 의 경우 지원하지않음.
# 그렇기에 TypeError 에 해당함.
#tu[1] = 4

# AttributeError: 'tuple' object has no attribute 'append'
#tu.append(8)

#삭제 :AttributeError: 'tuple' object has no attribute 'pop  
#tu.pop(1)