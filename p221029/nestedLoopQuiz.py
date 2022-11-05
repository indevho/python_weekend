#[구구단 2단 ]
# 구구단 전체 

#[문제1]
for i in range(1,10):
    for j in range(1,10):
        print(f'{i} x {j} = {i*j}')
    print()


#[문제2 짝수단만]
print("2222")
for i in range(1,10):
    if i %2 ==0:
        for j in range(1,10):
            print(f'{i} x {j} = {i*j}')
        print()


#[ 짝수단인데 ,짝수까지]
print("3333")
for i in range(1,10):
        #[print(f'{i} x {j} = {i*j}') for j,j2 in enumerate(range(1,10),1) if j<=i and i%2==0]
    [print(f'{i} x {j} = {i*j}') for j in range(1,10) if j<=i and i%2==0]
        
        #for j in range(1,10):
        #    if j<=i:
        #        print(f'{i} x {j} = {i*j}')
    print()

#[print(f'{math.index(r)+1} 번 학생은 {r} 점으로 합격입니다.') 
# for r in math if r>=60]

# 너무 지나친 중첩에 대해서,  
#  내가 생각한 방법을 반추하고, 한번 변환된 방식을 트라이해봐야한다






