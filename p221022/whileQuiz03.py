# 문제3  정수를 입력받은후 덧셈결과를 출력한다. 
sumNumber= 0
while True:
    

    addNumber = int(input())
    sumNumber += addNumber
    if addNumber == 0:
        print('합계>> ',sumNumber)
        break

