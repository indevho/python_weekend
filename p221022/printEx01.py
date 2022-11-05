## print함수
# print( 값, 값 )
#help(print)
import os
# sep 언급 안했으므로 sep 은 ' ' 디폴트값이다. 
import sys


print ('one','two','three', end='\n1\n2\n3')
# sep 이 더이상  ' ' 디폴트가 아니라 __ 이다.
print ('one','two','three',  sep='>>', end='/')

print('출력합니다.', end='\n\n')# default   '\n' 이 들어옴
print('다다음줄에 출력합니다. ')


print(sys.stdout)
# 표준 출력 장치 - 모니터, 프린터 등이있으나, 모니터에 나오게되는것.
#표준출력장치(stdout) :  화면에 띄워 줘.  터미널 기준으로, 최선의 방법으로 띄워 줘.
#이걸 다른것으로 바꾸면.  메모장으로 내보내버릴수있다.
#  파일 옵션을   출력 대상으로 한다.
folderUrl= 'D:\python\workspace\\newFolder2'
try:
    os.mkdir(folderUrl)
except:
    print('폴더 이미 있음')
sample = open(folderUrl+'\samplefile1234.csv', 'w')  
print('GeeksForGeeks','sadasda','asdasd',sep=',', file = sample)
print('GeeksForGeeks','sadasda','asdasd',sep=',', file = sys.stdout)
print('111111','222222','33333',sep=',', file = sample)
print('111111','22222','333333',sep=',', file = sys.stdout)

sample.close()

# ??  다른 디렉토리에 넣고 싶다면 open 에 어떤 걸 먹여줘야하는가