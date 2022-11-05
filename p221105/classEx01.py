'''

클래스는 자료형이다. 

자료형 int  float str 

클래스다른말로 사용자정의 자료형이라고함 
사용자정의 참조자료형 

클래스 안을 채울수 있는 것들 : 멤버
변수 또는 함수가 멤버로 활동가능 


클래스 정의 
class 클래스명:
    멤버
    멤버 


객체 인스턴스  생성 ? 

변수 =  클래스명() 

메모리는 주소라는 것 있고. 



'''

class Student:
    #멤버함수 : 메서드 올수있지요
    #name = ''
    def setName(self, name):
        self.name = name
    def greeting(self):
        print( self.name+ ' 님 안녕하세요',self)
    def infoPrint(self):
        print('제 이름은 '+self.name + '입니다 ')
        print('self address >> ',self)


# 객체 인스턴스 생성 ( 클래스 멤버 영역 X )
hong = Student() 
# hong 주소값이 저장이 된 변수 즉 참조변수 
print(hong) # ~F150
hong.setName('홍!')
hong.greeting() # ~F150
hong.infoPrint()

park = Student() 
# hong 주소값이 저장이 된 변수 즉 참조변수 
print(park) # ~F150
park.setName('팍!')
park.greeting() # ~F150
park.infoPrint()
