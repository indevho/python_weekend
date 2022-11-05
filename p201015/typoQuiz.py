from operator import indexOf
from re import I


number =  [100,200,100,500,200,600,300]

#[문제1]
# 중복 값을 제거하고,  오름차순 정렬하기
# tempSet =(set(number))
# tempList = []
# tempList = list(tempSet)
# tempList.sort(reverse=True) 
# print(tempList)
# print(type(tempList))
## 정답
print('중복 제거 >>' , list(set(number))) # 사본으로 작업한 것
#print('number >>' , number)# 원본 이 영향 받아야지
number =  list(set(number))
print('number >>' , number)# 원본 이 영향 받아야지



#[문제2]
# 요소 300 뒤에 400 을 추가하게 하시오 
## 요소가 아무리 많아도 , 300 이 가운데 있든 어디에있든, 그뒤에 400 이들어가도록 해야한다.
number =  [100,200,300,500,200,600]
#number.insert(  indexOf(number,300)+1,  400)
# number.insert(-2, ['a','b'])
#print(number)

# 정답
index = number.index(300)
print('요소 300의 위치 > >', index)
number.insert( index+1 ,400)
print('400 추가 number >> ', number)

# 300 이 여러개면? 

