import re



file = open('D:\python\workspace\p221105\ex.txt', 'w',encoding='utf8') # 그냥 파일명만 있으면 , 상대 경로에 파일이 생긴다. /
s = '한글만 찾을래요. 漢子는 싫어요. abc우리1200-파이선? python'
hangul = re.compile('[\uac00-\ud7a3]+')

result= hangul.findall(s)
print(result)
for i in result:
   print (i , file= file)

file.close()