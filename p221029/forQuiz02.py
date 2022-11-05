math  = [90,45,60,75,50,90]
# 수학 점수가 60 이상인 학생 점수출력 
# 가장 첫번째로 저장된 , 배열상에 출석 번호가 있다고 보면 된다 
#  n 번학생은 m 점입니다


#three = [r for r in range(1, 100)  if r%3 ==0 ]

[print(f'{math.index(r)+1} 번 학생은 {r} 점으로 합격입니다.') 
 for r in math if r>=60]

 # 중복 점수가 있으면? 어떻게 걸러내는가



 #정답 
#  학생번호 index 
# 리스트 내포 문법으로 가능 한 것인가???
index = 1
# 60 이상인학생점수, 번호출력 
for m in math:     
    if m >= 60:
        print(f'{index} 번 학생은 {m}점으로 합격입니다 ')
    index = index +1 


#[print(f'{math.index(r)+1} 번 학생은 {r} 점으로 합격입니다.') 
#for r in math if r>=60]

