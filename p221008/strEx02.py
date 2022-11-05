'''
[문자열 함수]
'''
st = '  Hello  '

## 문자열의 길이 
print('문자열의 길이 >> ', len(st))

## 특정 문자열내의  문자 몇개인지 
#   str.count(문자)
# is case sensitive
print('l 의 갯수 >> ', st.count('l'))

# 크롤링을 하게 되면 공백 제거를 '많이' 하게됩니다. 
# 공백 제거

##1 왼쪽 공백제거   문자열.lstrip()

##2 오른쪽 공백제거  문자열.rstrip()

##3 양쪽 공백제거   문자열.strip()

## 내부 공백 제거는 x 
print('|'+ st + '|')
# list 에서 본 리스트 덧셈 연산자와 동일 

print('|'+ st.lstrip() + '|')
print('|'+ st.rstrip() + '|')
print('|'+ st.strip() + '|')

#대소문자 변경
# [문법] 
# 소문자들을 대문자로 변경   문자열.upper()
# 소문자들 대문자로 변경   문자열.lower()
print('원본|'+ st + '|')
print('upper|'+ st.upper() + '|')
print('lower|'+ st.lower() + '|')
# upper, lower 모두 복사본에 대한 작업이고 원본 수정안한다

# 2) index 문법
st ='  Hello  '
print('e의 위치 찾기 1_첫번째로나오는e ', st.find('e'))
print('e의 위치 찾기 2_첫번째로나오는e ', st.index('e'))


print('p의 위치 찾기 1_첫번째로나오는e ', st.find('p')) # 얘는 없어도 에러가 안남 -1
# find 가 좀더 친절하다 
#print('p의 위치 찾기 2_첫번째로나오는e ', st.index('p'))# 얘는 없으면 에러가 남


# 특정 문자를 골라서 변경해버린다. 
# 문법 :replace('old','new')

print('before ello > i ', st)
st.replace('ello', 'i') #적용이 안됨. 이것또한 사본상 작업이다.
print ('after ello > i ', st)
stCopy = st.replace('ello', 'i')
print('after ello > i ', stCopy)


# 문자열을 쪼갠다 
#   st.split( )
#  split 의 매개변수 , 나누는 기준이 된 문자는 결과에서 사라지고 , 
# 그 앞뒤 요소문자열만  "리스트" 형태로 나온다.

print('e 기준으로 문자열 나누기 ', st.split('el'))

# 문자열 결합하기 join 
# 결합하기X   특정 문자를 추가 (삽입)  
#  그냥 뒤에 삽입인가?  위치 지정한 삽입인가? 
# '추가할문자'.join(기존문자열)
#   join 의 매개변수에는 문자열도 되고, 리스트, 등 여러값 넣을수있다. 
# ~ 을  join 하는데, 사이사이마다 ~ 가 들어간다.

print(' 물결을 추가한다 >>','~'.join(st))

print(st.join('~'))







