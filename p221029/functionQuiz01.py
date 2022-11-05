# [문1 ] 사칙연산 보여주는함수정의 
def four_rules(n1, n2):
    print(f'{n1} + {n2} = {n1+n2}')
    print(f'{n1} - {n2} = {n1-n2}')
    print(f'{n1} * {n2} = {n1*n2}')
    print(f'{n1} / {n2} = {n1/n2}')


print('문제1 > ',str(four_rules(5,5)))


#[문 2]  인수로 정1수 1 입력 호출시, 입력된 인수값만큼 별 반복되는 출력함수


def star_count(n):
    print( '문제2 > ' , '*' * n )

star_count(5)


