import math
num =6

#[문제1]
# 변수 num의 값이 양수인 지 음수인지 0 인지 구분해서 출력하기 

if num >0:
    print('양수입니다')
elif num <0:
    print('음수입니다')
else:
    print('영수입니다')

#[문제2]
# 같은 변수 num 값이 짝수/ 홀수 출력
if  num% 2 == 1 : #num/2 == 1:
    print('홀수입니다')
else:
    print('짝수입니다')
#[문제3] 
# 값의 범위 출력합니다.  
if num<0:
    print('0 미만의 수')
elif len(list(str(num))) == 1:
    print(list(str(num)))
    print('0이상 10미만의수')
elif list(str(math.floor(num/10)))[0] == '1':
    print(list(str(math.floor(num/10))))
    print('10이상 20미만의수')
elif list(str(math.floor(num/10)))[0] == '2':
    print(list(str(math.floor(num/10))))
    print('20이상 30미만의수')
else:
    print(list(str(num/10)))
    print(list(str(math.floor(num/10))))
    print('30 이상의 수 ')
##

import math
num =6

#[문제1]
# 변수 num의 값이 양수인 지 음수인지 0 인지 구분해서 출력하기 

if num >0:
    print('양수입니다')
elif num <0:
    print('음수입니다')

else:
    print('영수입니다')



#[문제2]
# 같은 변수 num 값이 짝수/ 홀수 출력
if  num% 2 == 1 : #num/2 == 1:
    print('홀수입니다')
else:
    print('짝수입니다')


#[문제3] 
# 값의 범위 출력합니다.  
if num<0:
    print('0 미만의 수')
elif len(list(str(num))) == 1:
    print(list(str(num)))
    print('0이상 10미만의수')
elif list(str(math.floor(num/10)))[0] == '1':
    print(list(str(math.floor(num/10))))
    print('10이상 20미만의수')
elif list(str(math.floor(num/10)))[0] == '2':
    print(list(str(math.floor(num/10))))
    print('20이상 30미만의수')
else:
    print(list(str(num/10)))
    print(list(str(math.floor(num/10))))
    print('30 이상의 수 ')
## 
'''
성능을 배려하면서도 간결한 조건 
number < 0
number < 10
number < 20
number < 30 
else


'''