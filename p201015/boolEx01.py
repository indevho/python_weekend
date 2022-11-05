# 논리형(=논리 자료형)
# value =True
# bool 불. 

value = True

print('value >>' , value)
# 정수  int 
print('정수 5의 논리값 >> ', bool(5))
print('정수 -1의 논리값 >> ', bool(-1))
print('정수 0의 논리값 >> ', bool(0))

# 문자열  str > 논리값
print(' bool 함수 str \'\' >>' ,  bool(""))
print(' bool 함수 str>>' ,  bool('sdasdsa'))
print('value >>' , not value)
print('value  type >>' , type(value))

# 3) 리스트> 논리값
print('[2,4] 리스트를 논리값 >>' , bool([ 2,4]))
print('[] 리스트를 논리값 >>' , bool([                           ]))
