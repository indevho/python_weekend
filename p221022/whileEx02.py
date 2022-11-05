'''
[break]
반복문 내에서 if 와 함께사용
반복문 돌다가, break 를 밟게되면 반복문 탈출

'''

idx =0
while idx<10:
    idx = idx +1 
    
    if idx % 3 == 0:
        print('탈출!>>',idx)
        break

    print('idx>>', idx)
print('==finished==')


## 반복문이 continue 를 만나면 , 조건 검사하러 위로 올라가지 않.
# continue 기능 : 조건부로 깍두기 만들기
idx =0
while idx<10:
    idx = idx +1 
    
    if idx % 3 == 0:
        #print('계속!>>',idx)
        continue#날 만나면, 내 아래의 while 영역은 없는셈치는것!

    print('idx>>', idx)
print('==finished==')





