# for 문 구구단 

[print(f'2 * {en} = {2*(en)}') for en in range(1,9,1)]


# for idx in range(1,10):
#     print(f'2 * {idx} = {2*idx}')

# for Ex 02 보세요

data = [(1,2), (3,4),(5,6)]
# for d in data:
#     print(d)
#     print(type(d))
tup= (1,2)

# 튜플을 분배 받아서 가져온다. 
# 반드시 그 튜플의 갯수과 숫자가 맞아야한다. 
# 3번째 튜플만  사이즈가 다른 경우 , 예외발생 
for first, last in data:
    print(f'first : {first} , last : {last}')
    print(type(first))
