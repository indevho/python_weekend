import os
import sys,datetime
# 파일 쓰기 시 open 함수 



file =  open('D:\python\workspace\p221105\ex2.txt','a' 
#,encoding=sys.getdefaultencoding()
)
#q별다른 설정안하면 
# window 의 스트림에서 디폴트 문자코드는 안 맞는다.
# 그래서 이렇게 깨지는것이다.

file.write('\n가나다~~!')
#encoding 해도 ,  탐색기에서 열면 한글 제대로 나오므로 걱정 x



file.close()
print(datetime.datetime.now())