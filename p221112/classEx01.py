'''
클래스는 자료형이다 

클래스는 멤버를 가진다.

변수 : 인스턴스 변수 (instance field) , 
    클래스 변수( class field )

메서드 : 클래스 내의 멤버로서 존재하는 함수

-[ 클래스 변수에 대한 정의]

해당클래스로 생성된 객체 ( 인스턴스 ) 가
  서로 공유해서 사용하는 변수다.

  객체 생성 없이 접근 가능 


  클래스가 메모리에 로드될 때 메모리 할당 
---------
[접근형태. 사용은 어케? ]

인스턴스변수( 객체 변수) 
    self ? -> 단일 개별 인스턴스 나자신의 주소 
    self.변수명
    메서드 내에서만 선언됨.

클래스변수( class 변수 )

    class.변수명  
    클래스 코드블럭 아래라면 어디든~ 


객체 생성의 순서 
메모리할당이 먼저 되고 
생성자가 실행이 되어야! 
비로소 시작 


'''


# [클래스 정의하자 ]
class Person:
    message = ' hello world '
    count = 0

    #인스턴스 생성을 위한 생성자 
    def __init__(s) -> None:
        Person.count = Person.count +1 
        print('현재 생성된 사람 수 >>', Person.count)
    def show(s):
        show = Person.message
        print(show)




a = Person() # 생성하는 순간 생성자 코드블럭 수행
a.show() # 호출하는 순간 메서드코드블럭 수행 



#메모리할당이 먼저 되고 

print('객체 생성 전이지만, 이미 메모리에 올려진 \n 클래스를 확인해보기 \n count : ', Person.count)

#생성자가 실행이 되어야! 
print( ' init 을 수행해서  사람을 추가해보자 ')
p1  = Person()
p2 = Person()
p3 = Person()   

# 이렇게 출력 만 해주어도 4로 출력이 되지요 
print('클래스 변수 출력 >> ' , Person.count)
# id 라는 빌트인 함수로 내 pc  상의 해당 객체의
# mem 주소를 확인해보기 
print ( 'p1에 저장된 주소 >> ', p1  )
print ( 'p1에 저장된 주소 >> ', p2  )
print ( 'p1에 저장된 주소 >> ', p3  )












