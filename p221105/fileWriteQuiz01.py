 

def writeNumber( listArg):
    #print(listArg)
    target = []
    target = listArg
    print(target)
    listArg.reverse() #리스트 본체가 뒤집어짐
    print(listArg)
    #file = open('D:\python\workspace\p221105\\number.txt', 'w', encoding='utf8')
    file = open('D:/python/workspace/p221105/number.txt', 'w', encoding='utf8')
    #print(len(listArg))
    while len(listArg) > 0:
        num = listArg.pop()
        #print(num)
        file.write('\n'+str(num))
    
    
    file.close()#할당 되었던 자원 해제하겠다
    print("<<< 쓰기작업완료")

# number.txt 파일, 오늘 폴더에 1~10 정수 쓰시오 
writeNumber(list(range(1,999)))