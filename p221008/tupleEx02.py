'''
str(123)

처럼  튜플도 리스트로 변경이 가능하다. 

튜플을 리스트로 바꾸어보자

'''

even= (2,4,6 )

newList = list(even)
print(even)
print(newList )
newList[-1] = 7
even = tuple(newList)
print(even)