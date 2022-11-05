## 사용자에게 정수 2개 입력받은 후 덧셈 결과 출력


'''
엔터로 2개 입력받기
'''
num1= input(' 정수 1개 입력 하세요')
num2 =input(' 정수 1개 입력 하세요')
# 일단 입력이 되면 문자열로 받습니다. 
'''
띄어쓰기로 2개 입력받기 
'''
# num1,num2 =  input('숫자 2개 입력해주세요').split()
# # 이순간 문자열이 리턴되므로.... 
# num1 = int(num1)
# num2 = int(num2)
 
#greaterOne = num1 if num1> num2  else num2
#print('큰값>>'  , greaterOne)
stringSum = num1+num2
intSum = int(num1)+ int(num2) 
print('덧셈결과문자열>>' , stringSum)
print('덧셈결과정수형>>' , intSum)


