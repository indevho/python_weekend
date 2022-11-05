# 짝을이루는 k,v 로 이어진 dict 
# 학생 이름, 수학점수가 짝궁. 
# 키는 중복 X 동명이인 x를 전제로 한다. 

math = {'일길동':90, 
    '이길동':45 ,
    '삼길동':60,
    '사길동':75,
    '오길동':50 }
# 수학 점수가 
# [print(f'{math.index(r)+1} 번 학생은 {r} 점으로 합격입니다.') 
#  for r in math if r>=60]
#[print(f'{r} 학생은 {math[r]} 점으로 합격!') 
# for r in math if math[r]>=60]


#[방법1] 키벨류 뭉치 들을 한번에가져오는 dict.items()
# for m in math:
#     if math[m] >= 60:
#         print(f'{m} 학생은 {math[m]} 점으로 합격입니다.')


# [방법2]
#print('math.items() >>', math.items()) 
# for m in math.items():
#     if m[1] >=60:
#         print(f'{m[0]} {m[1]}')

# enumerate 활용 
print(type( enumerate(math) ))
# enumerate class 가 있다. list 는 아니다.
# enumserate 는 시작값을 지정해줄수 있습니다.
# 무조건 1씩 양의방향으로만 증가. 오직 startvalue int만 허용됩니다.
#for index,m in enumerate(math , 1):
#    print(m)
#    print(index)
math = [90,45,60,75,50]
for index,m in enumerate(math , 1):
# 딕셔너리를 매개변수로 받아서 enumerate 돌리면, 
    if m >= 60:
        print(f'{index} 학생은 {m} 점으로 합격입니다.')
    index= index +1









