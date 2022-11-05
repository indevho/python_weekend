'''
리스트
여러값을 묶어서 한 변수 내에서 인덱스를 붙여서 관리한다. 



'''
data  =  [2,4,6,8]
#data.append('3')
# 리스트의 길이 추출한다. 
print( len(data))
# 요소 = element = 원소 

#print(data)
#data.clear()
#print(data)

## 인덱싱
print('첫번째요소추출 > .', data[0])
print('마지막 요소 추출 ',data[-1])


##슬라이싱
print('첫번째~두번째 요소 추출 1  >> ', data[0:1])
print('첫번째~두번째 요소 추출 2 >> ',data[:3])# 생략일 뿐 바로 위와 동일

print('t(미생략_거의쓰지x)  세번째에서 마지막까지 추출 1)', data[2:4])
print('t(생략_일반적     )  세번째에서 마지막까지 추출 2)', data[2:])
print('t(생략_일반적     )  세번째에서 마지막까지 추출 3)', data[-2:])
# 같은 결과를 만들어 내기위해서 , 누가 작성했냐에 따라 각자 아이디어도 다르고
# 작성법도 다르기때문에 내부터 잘하는것이 중요.

number = [1, 3, [11,13,15] , 5, 7, 9]
print(len(number))
'''
The argument may be a sequence 
(such as a string, bytes, tuple, list, or range) or
 a collection (such as a dictionary, set, or frozen set).

'''

##리스트 변수 number 의 리스트를 추출 

print('리스트 요소 추출 +접근', number[2])
#number라는 리스트의 몇번인덱스에 해당하는 메모리 주소의 값 땡겨옴 
print('리스트 요소 추출 -접근', number[-4])
print('리스트 속 리스트의 마지막 요소 가져오기 >> ', number[-4][-1])
print('리스트 속 리스트의 13,15 뽑아오기 >> ', number[-4][-2:])
print('리스트 속 리스트의 13,15 뽑아오기  ', number[-4] )

 



squares = list(map(lambda x: x**2, range(10)))
'''
map(lambda x: x**2, range(10))
 
'''
print(squares)















