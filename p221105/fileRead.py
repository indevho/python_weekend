'''
READLINE - STR 한줄 
READLINES - LIST 전부
READ -  STR 전부 

open 함수는 - 디폴트 'r' 읽기 모드입니다.그러나 명시가 좋겠다.

'''

# 오픈
gugudan = open('D:\\python\\workspace\\p221105\\gugudan.txt', 'r', encoding='utf8')
# 읽기 
 
line = gugudan.read()
#print(line)
print(type(line))
print(line[:5])
print(len(line[:]))
print(line[:858])
#종료 

gugudan.close()