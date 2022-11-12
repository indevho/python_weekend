#전역변수
value = 5

#함수정의
def show():
    print('show() 함수 호출 되었습니다. ')


#클래스정의
class Increment:
    #메서드 멤버 
    def printNum(s, num):
        #인스턴스용 변수
        s.num = num + 1 
        print('1 증가된 값:  ', s.num)