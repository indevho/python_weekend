# 오픈
gugudan = open('D:\\python\\workspace\\p221105\\gugudan.txt', 'r')
# 읽기 

#while True:
lines = gugudan.readlines()
print(type(lines))# 단일 배열이다
for i in lines:
    print(i, end='')
        #if not line: # line == '' 도 가능!  ''은 False 논리값이다! 
    #break

print(gugudan)

#종료 

gugudan.close()