'''
 아래 요소에서 hi 요소 찾아서 hello 로 변경한다. 
'''

#data = [100, 200, 'hi', 'good', 300]
##code
# 단, hi의 위치가 다른 곳일 때에도 실행이 되어야한다. 
#print(data)

def solution(arr):
    data = arr
    targetIndex = data.index('hi')
    #print(targetIndex)
    #data[targetIndex]  = 'hello'
    data[targetIndex:targetIndex+1] = ['hello']
    print('최종결과 >> ',data)

solution([100, 200, 'hi', 'good', 300])    

'''
해결방법 1 
1)  idx를 가져온다.  data.index('hi')
data[idx] = 'hello' ( assign )

2) data[data.index('hi')] = 'hello'

해결방법2 
'''




# 근데 hi 가 1개 이상이고, 순서도 무작위면? 
def solution_multi(arr):
    data = arr
    #for a in data
    hiFlag = True
    hiIndex = 0
    while(hiFlag):
        try:
            hiIndex = data.index('hi')
            data[hiIndex:hiIndex+1] = ['hello']
        except:
            hiFlag = False

    #targetIndex = data.index('hi')
    #print(targetIndex)
    #data[targetIndex]  = 'hello'
    #data[targetIndex:targetIndex+1] = ['hello']
    print('최종결과 >> ',data)

solution_multi(['hi', 200, 'hi', 'hi', 300])    

