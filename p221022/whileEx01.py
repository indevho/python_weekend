'''

반복문 while 

파이썬은 들여쓰기로 
 영역, 코드블록을 인식한다. 
 파이썬도  그 영역 indent 기준으로 돌기 때문에.
 while 이 영향력을 행사하는 구역

  WHILE 뒤의 조건이 True 일 동안에만 반복된다.  \

while 의 내부 로직까지는 못봐도 . 
while 을 제대로 쓰기위한 전제조건이있다. 
  # 조건문 내에 쓰일 값은 모두 정의 되어있어야 한다. (상수든 변수든)
  #  True 또는 False 를 밷어내는 조건식이어야만 한다. 
'''

num =1 
while num<4:# num 이 4가되는순간 다음 '영역'으로 넘어감
    
    num= num+1
    print('num>>', num)

print( '=' * 20)
print('실행 완')    
print( '=' * 20)