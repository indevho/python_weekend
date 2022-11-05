'''
# 리스트내포
# 명령어 for 변수 in 여러값 ( iterable  )
'''


even = [2,4,6,8]
# d아래 와 동일한 결과를 내는 코드가있다.
#for en in even:
#    print(en)

#리스트 내포 
# 대괄호는 필수! 
# for 앞에는 실행부를 작성한다.
print('리스트 내포 start')
[ print(en)
 for en in even]
'''
 레인지를 돌면서 리스트에  append 가 있는 것입니다. 
 리스트에 원하는 값을 자동화해서 넣어주고 싶은거에요 
 리스트의 요소 추가를 간결한 코드로 실행해줄수있는것입니다. 
 이걸 정직하게 for 써서 한다면 
 ## 일반 for 문인데, 리스트 내포와 비교 해보기  
 evenTwo = [] #2
 for r in range( 2,11,2):
    evenTwo.append(r)
'''
 ## 
#형태2 
even =  [r for r in range(2,11,2)] 
#even =  r for r in range(2,11,2) 
# 대괄호가 없으면 안된다. 
print('even >> ', even)
print('even 자료형 >>' , type(even) ) 


##리스트 내포 3번째 형태 , if 문도 세팅해줄수 있음. 
# 리스트 내포 
three = [r for r in range(1, 100)  if r%3 ==0 ]
print(three)

# 일반 for 로 한다면 
three2 = []
for r in range(1,100):
    if(r%3 ==0):
        three2.append(r)

print(three2)

