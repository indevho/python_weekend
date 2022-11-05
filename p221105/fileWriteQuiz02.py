# number 2 파일 만들어서 
# 1~100 정수를 파일에 쓰시오 .

file = open('D:/python/workspace/p221105/number2.txt','a',encoding='utf8' )
for i in range(1,101):
    file.write(str(i)+' ')
    if(i%10 ==0):
        file.write('\n')


file.close()
