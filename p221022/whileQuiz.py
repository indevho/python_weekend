##[ 문제1 ]
## 구구단 2단 출력하기 
number=1
# 접근 : 변하는 것과 변하지 않는것을 선택
#  변하는 것이라면 변하는 방향 + - 를 선택
while number < 3:
    
    gop = 1
    while gop <10:
        print(number,'*',gop ,'=',number* gop)

        gop = gop + 1
    number = number +1
print('===================')
# 모범답안 
index = 1
while index <10:
    #깔끔하게 f문자열 로 작성하기
    print(f'2 * {index} = {2 * index}')
    #주의필요  + 를 쓰는경우에 ! 
    #print('2 *' + index + " = " + 2* index )
    #print('2 *' + str(index) + " = " + str(2* index) )
    # str 함수 처리 해주어야만 한다
    index = index + 1 
print('===================')




## [문제 2 ]
# 1~ 10 합 찾기 
initNum = 1 
untilNum = 10
# 주의!  sum 은 빌트인으로 이미 존재하는 것이므로 
# sum 을 변수명으로 쓰지 아니한다.
sumNum = 0

while initNum <= untilNum:
    sumNum = sumNum+ initNum
    initNum = initNum +1
print('1~10의 합',sumNum)

print(type(range(1,11)))
addTwo = sum(range(1,11))
print(addTwo)


