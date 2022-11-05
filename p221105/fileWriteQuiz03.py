# QUIZ 03 
# gugudan  2단~ 9단 만드세요 

file = open('D:/python/workspace/p221105/gugudan.txt','w',encoding='utf8' )
for i in range(2,10):

    for j in range(1,10):
        file.write(f'{i} x {j} = {i*j} \n' )
        if(j ==9):
            file.write('\n')


file.close()
