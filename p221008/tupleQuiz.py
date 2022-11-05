ex = (2,4,(1,3), [10,20,30])
## 1 튜플 변수 ex의 길이 구하기
print('문제 1 : 튜플의 길이 >>', len(ex))

## 2 튜블 변수 ex의 리스트 요소에 40을 추가하기.
#ex[3].append(40)#이건됨
#ex[3].insert(3,40)#이건됨
#ex[3].extend([40])#이건됨
#ex[3] = ex[3] + [40] #이건 안됨..
#TypeError: 'tuple' object does not support item assignment
#ex[3][-1:] = [40]#틀림, 마지막요소 30이 40으로 대체됨.. 
#ex[3][-1:] = [30,40]#맞음, 그러나 별로다
#print( ex[3]+ [40])
print( '문제 2 결과 >> ',ex )

print(type(ex[3]))
print(type(ex[3] +[40]))







