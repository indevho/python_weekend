# 문자열 사이에 존재하는 공백을 제거

quizOne = 'He  ll o'
print(quizOne.replace(' ',''))


# 문제 2  
numbering = 'a23 - 23456 - bc321'
# 이중에서 하이픈 기준으로 해서 3개 숫자 문자 조합 한
#  
print(numbering.replace(' ','').split('-')[1])
 

 