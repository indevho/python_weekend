'''
큰값출력하기.
출력형태

'''

n1,n2=5,5

# arr=[]
# arr.append(n1)
# arr.append(n2)
# arr.sort(reverse=True)
# print(arr[0])


# 방법1 조건문 
if n1> n2:
    print('큰값 >>', n1)
elif n1<n2:
    print('큰값 >>', n2)
#else:
#    print('값이 같습니다.')
# ??1 
# 5=5 인 경우에는 그냥 아무런 라인도 수행하지 않음. 
#  예외가 발생하는것도 아님 


# 방법2 조건 연산자 
# True 일때 if 조건식 else False 일때 
print( print('큰값2 >>',n2)  if n1<n2 else print('큰값2>> ',n1)  )
#??2
# 여기서 바깥 print 가  None 을 밷어내는 이유?   
# print 는  반환값이 None 인 함수이기 때문에? 

# 모범답안
maxValue =  n1 if n1> n2  else n2
#  XX if trueFalse else YY  가 하나의 덩어리이다. 
print('맥쓰발류',maxValue)

# 조건 연산자 + 포맷팅 응용
year = 2000
isLeapYear = year%400==0 or year%4==0 and year%100
print('{0}년은 "{1}"입니다.'.format(year,'윤년' if isLeapYear else '평년'))
print('{0}년은 "{1}"년입니다.'.format(year,'홀수' if year%2 else '짝수'))














