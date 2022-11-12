
# 그냥 쓰면 define 안되있다고 하지요 .
#print('value >> ', value)


#형태  1 
from pack import ex
import pack.ex  # pack.ex.value 로 써야함
print( ex.value)



a = ex.Increment()
a.printNum(1)

from pack.ex import show, value
print('형태 2= ==============')
print( 'value 멤버도 출력해보자 > ' ,value)
show()

