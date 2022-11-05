'''
Is  str  iterable?

Method 3: Using the iter() builtin function.
The iter built-in function works in the following way:

Checks whether the object implements __iter__, and calls that to obtain an iterator.
If that fails, Python raises TypeError, usually saying “C object is not iterable,” where C is the class of the target object.
'''


st= 'Hello'

print('  변수 st의 타입> ',st)

## 문자열 인덱싱
print('첫 문자 추출 >> ', st[0])
print('마지막 문자 추출 >>', st[-1])

##  문자열 슬라이싱 
#print('ell만 추출 >> ', st[-4:-1])
#print('ell만 추출 >> ', st[1:4])
print('ell만 추출 >> ', st[1:-1])
#print(iter(st).__str__())
#print(iter(st).__sizeof__() )


## 인덱스 1과 3에 대항하는 문자 잘라내기 
print( 'el만 추출 >> ', st[1:4:2])

fruit = '하나둘셋넷'
# 나, 셋 만 추출 해보기 
print( '나셋 추출 >> ' , fruit[1:4:2])
# [1:4:2]  ->> 1에서 4까지 2씩 추출하세요. 수열의 개념.


#print('인덱스골라서 h l o 만 추출 >> ',st[0:5:2])
#print('인덱스골라서 h l o 만 추출 >> type ',type(st[0:5:2]))
# 0번 인덱스에서 ~ 5번 인덱스 미만까지 해서  2 간격으로 뽑기 
print('h l o 만 추출 축약 버전 ', st[::2])
#  return as STR



## 추가문제  olleH 형태로 추출하기
newList = list(st)
print(newList)
#newList=  newList.sort() 
#print(newList)
result = []
while(len(newList) != 0):
    result.append(newList.pop())

print( result )
resultStr = str(result)
print(type(resultStr) )
print('>>>', resultStr )
#print(st)
print( '>>> ', st[::-1]) # String 뒤집기 
#알아서 시작 지점을 -1 로 잡는것
print('>>> ', st[-1:0:-1])# olle
print('>>> ', st[-1: :-1])# olleH
##생략 없이  olleH 구현 방법은???
























