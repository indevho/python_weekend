even= [2,4,6,8]
##인덱싱
print(even[1]) 
print(type( even[1])) 

# 라인 복제 후에 type 확인하기 
print(even[:2])
print(type(even[:2]))

## 슬라이싱 -->> return as a list type 
print('슬라이싱 type1 값>>', even[:2])
print('슬라이싱 type1 >>', type(even[:2]))
print('슬라이싱 type2 값>>', even[:1])# 0번째 인덱스 값만 가져옴
print('슬라이싱 type2 >>', type(even[:1]))




print("11111===========================")
numbers = [1, 3, [11,13,15] , 5, 7, 9]
for i in numbers:
    #print(isinstance(i,int) )
    if isinstance(i,list):
        print('  is list >>>'+ str(i))
    if isinstance(i,int):
        print('  is int >> '+str(i))
print("222222===========================")
for i in numbers:
    #print(isinstance(i,int) )
    if type(i) is list:
        print('  is list >>>'+ str(i))
    if type(i) is int:
        print('  is int >> '+str(i))