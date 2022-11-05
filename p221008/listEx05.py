data= ['one','two','three']
print('요소 변경 전>> ',data)
data[1] = 2 
print('요소 변경 후>> ',data)


#data[0] = [5,7]
#print('여러 요소 변경 후 > ',data)
# 요소 하나 추가를 해버림
# 요소 2개 추가를 하고 싶다면 어떻게?? 
# 인덱싱 . - data[0] 이 가리키는 대상이 단일 요소였던 것 뿐이다 즉 접근이 잘못된것.

data[:1] = [5,7]
# 뭐가다르냐 data[0] 은 타입이 단일요소 int 이고 
# data[0:1] 은 타입이 list 이다..
print('여러 요소를 넣은 후 >> ',data)
# wow ..... 

# 2와 three 를 지워서 9 단일값으로 바꿔보기 
#data[-2:] = 9 # Error , 역시나 list 로 담아 주어야 한다. ( only assign iterable )
data[-2:] = [9]
# 기존 리스트의 [2,'three'] 의 자리를 [9] 로 대치해주세요.
print(data)