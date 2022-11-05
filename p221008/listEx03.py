# 리스트 연산자 
'''
+ 연산자 : 요소 추가  
* 연산자 : 요소 반복  

'''

odd = [1, 3, 5]
# 우리 실무에서는 파일이나 웹에있는 걸 가져오게 된다.
even = [2,4,6]
sumOddEven = odd+even
print('+ 연산자 > ' , odd + even)
print(' sumOddEven > ' , sumOddEven)
print(' * 연산자 >> ', ( odd * 3 + even ) * 2  +  even + even )
print('odd >>' ,  odd )
print('even >>' , even)
  # 원본 아닌 복사본 간의 결합의 결과를 보여주는 것임 .


# odd 에 even 의 요소를 추가 
odd = odd+even
print( '정답 newodd : ', odd)

