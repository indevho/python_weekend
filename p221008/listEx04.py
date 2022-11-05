# def findIndex(arr,str):
#     try:
#         print('two 요소의 인덱스>> ', arr.index(str))
#     except:
#         print('ValueError:'+ str(str) +' is not in list')


#[ 리스트에서 제공되는 함수]
data = [5,1,7,3,9]

##정렬 오름차순하기 .
##문법. 함수 사용하듯이 쓴다. 
# 리스트.sort() 
print('정렬 전 >>', data)
data.sort(reverse=False) 
# 매개 변수로 reverse=True 먹여주면  내림차순 정렬 해준다.
print('정렬 후 >>',data) 
#  list.sort returns  None 

#정렬 : 역순 
# 리스트.reverse()

print('역정렬 전 >>', data)
data.reverse()
print('역정렬 후 >>',data)


# 특정 요소의 인덱스 추출하기 
# 문법  :리스트.index(요소값)
number = ['one','two','three','four']
#print('two 요소의 인덱스>> ', findIndex(number,'tow'))
try:
    print('two 요소의 인덱스>> ', number.index('tow'))
except:
    print('예외발생!  ValueError:'+ str('tow') +' is not in list')
print('two 요소의 인덱스>> ', number.index('two'))


#요소 추가 : 단일 요소를 마지막 인덱스에 덧붙여 주는 함수
#문법 :   list.append( x )
number.append('five')
print('요소 five 추가 후 number> ',number)

#요소 추가 :여러개 값을 마지막 위치에 추가한다. ( 다량 을 덧대주기 + 랑 다른게 뭐지 .. )
number.extend(['six','seven'])
print('여러 요소 추가 후 number> ',number)


#주의 
# number.append([8,9])
# print('주의 >>', print(number))
# append 의 역할을 상기 :  리스트에 단일요소를 추가해주는 역할이다. 


'''
 what if - 원하는 위치에 추가하고 싶으면? 
#문법 list.insert()
# 매개변수로 2개의 값을 받는다. ( 인덱스, 값 ) 
'''
number.insert(2,'five')
print(  '인덱스 2 의 자리에 값을 강제 삽입 결과',number)
# insert 가   append 를 대체 할 수 는 없다.
# number.insert(-2, ['a','b'])
# print(number)

#요소 갯수 : 특정요소갯수
# list.count(요소)
print('요소 five 개수 ', number.count('five'))

# 요소 삭제 해주는 함수
# 리스트.remove(요소)
'''
전제조건 : 이 리스트 안에 뭐가 있는지 내가 알고있다.
'''
print('리스트 길이 :' , len(number)) 
# 이 함수도 요소 타입상관없이 다쓸수있다.
number.remove('two')
print('요소 two 삭제 후 >>  ',number)
print('요소 two 삭제 후 길이 >>  ',len(number))

number.remove('five')
number.remove('five')
# solution : 두번 써라
print('요소 five 삭제 후 >>  ',number)
print('요소 five 삭제 후 길이 >>  ',len(number))

# 요소 삭제하기 
# 문법  리스트.pop(인덱스넘버)
# 전제 : 나는 구체적으로 요소값이 뭔지 모르고, 그냥 몇번째 애를 지우고 싶다.
number.pop(2)
print('인덱스2 자리에있는 요소 삭제 후 ', number)

# 매개변수 없이 pop 사용 시 ?  
# 미지정 pop() > 가장 마지막 요소 삭제
#number.pop()
print('그냥 매개변수없이 pop() 사용 튀어나온놈', number.pop())
print('그냥 매개변수없이 pop() 사용 튀어나간결과', number)
