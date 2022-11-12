'''
모듈
MODULE 

이미 만들어진 파이썬 파일
변수 함수 클래스를 "모아" 놓은파일 

모듈 가져오기 
import 

[형태1 ]
import 모듈명  -> 이 이름에 해당하는   py 파일을 끌어다 쓸래 ! 

[형태2 ] 
from 모듈명 import 변수명,함수명, 클래스명 
>>  특정 py 파일 내의  함수만 끌어다 쓸래 !

[형태3 ] 
import 모듈명 as 별칭 
'''


#형태1  
#import random 

# 이 random.py 내의 random을 땡겨서 써보자
#print('랜덤값 , ' , random())  #  'module' object is not callable 
#  그냥 random() 을써버리면,  모듈을 마치 callable 인양 쓴게 되는데, 
#  거부당한 것이다. 파이썬은 이 random 을 모듈로 인식하지, 함수로 보고있지 아니함.
#print('형태 1 호출 랜덤값 , ' , random.random())
# 호출 될때마다 0~1 사이 무작위수를 내밷는다.




#형태 2
from random import random

# 형태2로 호출하기 
print('형태 2   호출 랜덤값 , ' , random())


# 형태 3 

from random  import random as r
print('형태 3   호출 랜덤값,  ', r()) 















