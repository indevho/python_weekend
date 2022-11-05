'''
집합
여러값 묶어서 하나의 이름으로 관리 
자료 set

형태: 중괄호 ,컴마 ( 딕셔너리는  콜론 )
{ val, va2 , va3}

중복된 값을 추가 저장 할수 없다.

저장로직에 ? 자료구조 상? 이미 있는지 확인하는 로직이 있구나

'''
a = {}
b = {1}
print(type(a))
print(type(b))

even = {2,4,6,2,8,4}
evenDc = {2:1,2:'s'}
print('even>> ', even)# 8 2 4 6 으로 나온다. 
print('even type>> ', type(even))
print('even>> ', evenDc)
print('even type>> ', type(evenDc))
#집합 활용시에는 >  특정 값을 뽑아내기 위해 쓰지는 않습니다.
# 실무 사용 빈도도 낮아요

s1 = {2,4,6,8}
s2 = {4,6,8,10}

## 합집합   |  또는   union함수 
print('합집합: 연산자>>' ,s1 | s2 )
print('합집합: 함수>>' ,s1.union(s2) )

# 차집합   -  또는    difference 
print('차집합: >> ' , s1.difference(s2))


print 
