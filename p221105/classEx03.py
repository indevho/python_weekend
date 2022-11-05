
'''
변수 종류 
- 전역변수
-지역변수


Class 내의 멤버변수 
- 객체변수 
- 클래스 classs 변수 ( 클래스명 .  ~   아래에 위치한다)
- 클래스변수는 클래스명으로 관리가 된다
- 클래스명 으로 접근한다
- [문법]  클래스명.변수   -  로 조작해준다

[인스턴스 (객체) 변수 ]
- 객체 각개로 존재한다
- 참조변수 통해 접근! 
-  self.변수명   으로 조작해준다

'''


class Person:
    ##클래스 변수 
    # 설계도 자체에서 관리되는 변수
    count =0 
    #클래스변수는 메모리에 먼저 들어와버린다

    def __init__(self ):
        print('사람객체 생성완')

    def info(self):
        # 객체 변수( 인스턴스변수!  ! ) 
        #print(f'현재 있는사람객체는 = {count} 개 입니다')
        Person.count = Person.count+1 
        print(f'현재 생성된 객체는 {Person.count}  개 입니다')
        # 클래스 본인의 count



        #try - except - finally 로 INFO() 호출 할때마다 값 올려주기 
        # try:                
        #     self.count = self.count+1 
        # except:
        #     self.count =1 
        # finally:
        #     print(f'현재 있는사람객체는 = {self.count} 개 입니다')

print(f'클래스변수 count >> {Person.count}')
p1 = Person()
p1.info()
print(f'클래스변수 count >> {Person.count}')
Person.count = 0
print('        0개 됨')
p2 =Person()
p2.info()
print(f'클래스변수 count >> {Person.count}')