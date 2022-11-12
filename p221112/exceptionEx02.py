n1,n2 =  eval(input('정수2개를 입력합니다>> '))


try:
    result1 = n1/ n2 
    result2 = n1 % n2 
except: 
    print('예외처리 에러')
else:
    print('예외 발생 안했네요 굳 ')
    
    print('몫 >> ', result1)
    print('나머지 >> ', result2)

finally:
    # 파이널리는 또 res 1, 2 를 모른다..
    #print('몫 >> ', result1)
    #print('나머지 >> ', result2)
    print('축 : finally 도달')

print('실행 완! ')