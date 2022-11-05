import os 
import sys
import datetime
'''
파일 쓰기 
1. open 함수,  mode  -w , a 
2. write 함수
3. close 함수


'''

#1. open 함수,  mode  -w , a 
# 문법 :    변수 = open('파일명 또는 경로 ', '모드')
file = open('D:\python\workspace\p221105\ex.txt', 'a',encoding='utf8') # 그냥 파일명만 있으면 , 상대 경로에 파일이 생긴다. /
 # iDE 는 경로 복사 쉽게할수있도록 기능 제공해준다.
 # w 새로 덮어쓴다
 # a  append 해준다
#D:\python\workspace\p221105
'''
fin1 = open(file1, encoding='utf8')
fout = open(outfile1,'w', encoding='utf8')
for line in fin1:
    print('utf-8=',line, file=fout)
위 처럼 출력 파일에 encoding만 선언해 주면 해결되는 문제인데

어느 책자에도 출력 파일을 열때 encoding을 해야 한다는 말이 없더군요. ^^
'''
# 만일 hd에 이 파일이 있으면 그걸 사용하고, 
# 없으면 새로 써준다 

# 쓰기위한 글들 내용물들이 지나다니는 통로가 RAM에 있고, 
# 통로가 오픈이 되면서  ram 의 내용이 hd 로 내려올수있게됩니다
# 그 공간을 스트림 stream 
# 통로가 만들어지는 것은 resource 자원! 

#print('hihihiㄴㅁㅇㅁㄴㅇ家ㅁㄴㅇㅇhii',file=file)
file.write("\ngood day!  "+str(datetime.datetime.now()))

#print('GeeksForGeeks','sadasda','asdasd',sep=',', file = sample)


#2. write 함수
file.close()




#3. close 함수

print('<<< 실행 완', sys.getdefaultencoding()) 
print('<<< 실행 완', datetime.datetime.now()) 