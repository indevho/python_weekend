list_value= ['100','good','5','250','hi','500']

list_number = []

#예외 처리 구문 이용해서, list value 요소중
# 숫자로된 문자열만 추출하기 


for i in list_value:

    try:
        list_number.append( str(int(i)) )

    except:
        pass


print('최종결과')
print(list_number)