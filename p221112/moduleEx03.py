
# FROM 은 형태가 다양하게 나올수있습니다. 



#형태  1 
from pack import ex
import pack.ex  # pack.ex.value 로 써야함 
from pack.ex import value 
print(value)

print( ex.value)



a = ex.Increment()
a.printNum(1)

from pack.ex import show, value
print('형태 2= ==============')
print( 'value 멤버도 출력해보자 > ' ,value)
show()
