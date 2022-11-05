'''
[딕셔너리]
 여러 값 들을 묶어서 하나의 이름으로 관리
 자료형 type ; dict 로 나옴.


형태  ( 중괄호,  콜론,  컴마)
{키: 값, 'name' : '홍길동', 'age' : 25}

key 를 타고 값에 접근해요 

방법이 그뿐이에요
요소의 순서를 보장하지 않기 때문에
여튼 메모리상에 순서를 넣어서 쌓아갈텐데 
그럼 그 순서를 어떤원리로 결정하나요? 
key 를 타고 들어가야하는것

dict 의 키는  엄격하게 내용을 구분한다
'1' 과 1 이 다르다.

'''

student = {1:123 ,'name' : '홍길동', 'age': 25, 'address': '서울 강남구'}
print( 'student(FULL) >> ', student)
print('딕셔너리 변수 student 의 type >> ',type(student))
print('딕셔너리 변수 student 의 길이 >> ',str(len(student)))
# kv 쌍이  한 단위가 된다. 
# dict 는 len 함수의 대상이 될수있다
print('이름',str(student['age']))
print("여기! ======")

print('student\'s name : {}' .format(student["name"]) )
print('student\'s name : {name}' .format(**student) ) # ** 접근법
print(f'student\'s name : {student["name"]}')
print(f"student\'s name : {student['name']}")
 
# format 메서드는 -->> 인자 또는 키워드 인자 에 대한 포메팅이 적용된다.



print("여기! ======")
print(f'{student}')
#print("\n".join("{}\t{}".format(k, v) for k, v in student.items()))
print("======")
#print("\n".join("{}\t{}".format(k, v) for k, v in sorted(student.items(), key=lambda t: str(t[0]))))
print('이름 >> ', student['name'])
print(' 인덱스 테스트 >> ', student[1])
# # 인덱스 불가! 순서보장X
# student 까보니까 > 어 딕셔너리네? 
#   1 이라는 키 가볼가?


#  딕셔너리 접근해서, 딕셔너리 자체의 값변경한다. 
# 이름을 홍길동에서 이미자로 변경 
# 기존 KV있는경우에는 덮어쓰기 함
print('before >> ' ,student)
student['name']= '이미자'
print('after >> ' ,student)

#  키를 못찾는 경우 할당
#print(student['phone'])
student['phone'] = '010-1111-1111'
print(student['phone'])

#  요소 삭제하기
#   del 딕셔너리[key]
print('주소 삭제 전 길이 >> ' , len(student)) 
del student['address']
print('주소 삭제 후 >> ' , student)
print('주소 삭제 후 길이 >> ' , len(student)) 

#key 만 뽑아오기 열쇠 주머니 가져오기
print(' key 추출 ', student.keys())
print(' key 추출  type  ', type(student.keys()) )
# 기존에는 배열로만 나왔는데,  dict_keys 클래스가 있네?
# 기본 자료형 기반으로 만든 별도의 자료형 . 클래스

#value 들만 추출 
print('value 추출 >>', student.values())
# type 을 눈여겨보기 :  dict_values
# 내부적으로는 리스트 이지만, 별도 타입을 붙여놓은 것이다. 
# 이유는 놓침.. 

# 딕셔너리 요소 단위 별로 다가져와요
print('KV동시추출', student.items())
# type 을 눈여겨보기 :  dict_items 
#  소괄호 안에 여러개 있죠. 튜플. 
# 튜플들이 담겨있는 리스트 형태이다.

## key 를 통해서 value 추출하기 
## student -> name 이미자
#print('이름>> ', student['name'])
#dict 에서 쓸수있는 함수 get 메서드  키값을 넣어준다.
print('이름>> ', student.get('name'))
print('  없는거 가져와>> ', student.get('1'))
print('  없는거 가져와>> ', type(student.get('1')))# class NoneType
# 굳이 왜 get 을 쓰느냐  null 처리를 위해서  hard 하게 가져오냐, soft 하게 가져오냐의 차이
# None 자료형 
# 없는 걸 가져오려고 하면 디폴트 값을 가져와준다
# None을 보고싶지 않을 때 , get 의 두번째 매개변수로  ifNull 값을 넣어준다.
print('이름>>',  student.get('1','이름없음')) 

# in 연산자 ? 
# 문법: 있니? 확인하기.  값 in 여러값(iterable)
print('address -키는-존재하는가? >>', 'address' in student)
print('name -키는-존재하는가? >>', 'name' in student)
#  존재여부 비교 in 의 경우 . 기본은 student 를 쓰면   student.keys() 와 동일.

#데이터 중에  이미자라는 값이 존재하는가? 
#print('이미자 값이 존재 하나요 >>', {'name':'이미자'}.items[0] in student) # 안된다..
print('이미자 값이 존재 하나요 >>', '이미자' in student.values()) 
# dict_values 도 - '여러값'  type 이기에 적용된다.
# print( 4 in 5 )#  in 뒤 의 값 is not iterable 
#print( 4 in (4) )# (단일값) 은 튜플이 아니다! iterable도 아니다
print( 4 in (4,2) )# (comma기준여러개) , {} , [] , '' 도 다 가능하다
print( type ( (4) ))
print( type ( (4,'') ))


#모든 요소 삭제하기 
# 딕셔너리.clear()
student.clear()
print('모든 요소 삭제 후 >>', student) # 빈 {} 값이 나온다.
print('모든 요소 삭제 후 type >>', type(student)) # 빈 {} 값이 나온다.
student2 = {}
print(type(student2))










