'''
with open() as 변수명:
    명령어
    명령어


'''

with open('D:\\python\\workspace\\p221105\\gugudan.txt', 'r', encoding='utf8') as gugudan:
    print(gugudan.read())
    print('================= END')
    #with 명령어 영역 탈출 할때 close() 가 호출됩니다!!

#실무에서  with 문 더 자주씁니다. 


# 오픈
gugudan = open('D:\\python\\workspace\\p221105\\gugudan.txt', 'r', encoding='utf8')
# 읽기 
 
line = gugudan.read()
#print(line)
#종료 
gugudan.close()

