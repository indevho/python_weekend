'''
Constructor  
객체 생성될때 무조건 하나의 생성자 ( 생성자가 여러개 될수있지만, 그중 단일개만 호출된다!! )
생성자는 '메서드' 로 분류가 된다

" 생성자는 메서드가 아니다! " 라는 관점도 있으나, 
기본적으로 메서드로 보도록 한다.
생성자명은 정해져있다 (언더바2개 앞뒤로 , 파이썬의 룰! )  

 __init__(self)

'''

class Student: 
    # construnctor   밟는 순간!   1.주소객체생성 >> 2. 생성자 메서드호출
    
    def __init__(self ) -> None:
        print('생성자 실행완료!')
        pass
    # __init__  덮어쓰기    
    # self 에는 알아서 주소가 들어올거고.  name 은 직접 넣어주세요
    def __init__(self , name , age) -> None:
        print('생성자 실행완료!')
        self.name= name
        self.age= str(age)
    #멤버함수 : 메서드 올수있지요
    #name = ''
    def setName(self, name):
        self.name = name
    def greeting(self):
        print( self.name+ ' 님 안녕하세요',self)
    def infoPrint(self):
        print('제 이름은 '+self.name + '입니다 '+ self.age + ' 살입니다')
        print(f'self address >> {self.age}')  

#  Student() 로 썼던 이유도 눈에 보이지않던 , def 생성자가 있었기 때문에 가능한 일이었다! 
# 객체 생성시점에 단 1번 실행 된다!
hong = Student('honggildong ', 98)
hong.greeting()
hong.infoPrint()
# __init__ 없이 Student('hong') 해버린경우
# TypeError: Student() takes no arguments 
# __init__(self) 만 있는데 Studnet('hong') 해버린경우
#  TypeError: Student.__init__() takes 1 positional argument but 2 were given
# 이 말에 따르면 self 도 하나의 positional argument 구나~ 

# __init__( self , name ) 인데  그냥 Student() 해버린경우
# TypeError: Student.__init__() missing 1 required positional argument: 'name' 

park =Student('박', 9)
park.infoPrint()


