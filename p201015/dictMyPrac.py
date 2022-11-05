student = {1:123 ,'name' : '홍길동', 'age': 25, 'address': '서울 강남구'}

print("\n".join("{}\t{}".format(v, v) for k, v in student.items()))

# generator object
print("{}\t{}".format(v, v) for k, v in student.items())
'''
iterable한 순서가 지정됨(모든 generator는 iterator)
느슨하게 평가된다.(순서의 다음 값은 필요에 따라 계산됨)
함수의 내부 로컬 변수를 통해 내부상태가 유지된다.
무한한 순서가 있는 객체를 모델링할 수 있다.(명확한 끝이 없는 데이터 스트림)
자연스러운 스트림 처리를 위 파이프라인으로 구성할수 있다.
(Java에서 파일스트림 처리시에 특정 바이트단위로 반복하는 것을 말하는듯..)
'''
# 1.   formatting str 로  gen 을 도출 한 뒤에 for 순회
for i in ("{}\t{}".format(k, v) for k, v in student.items()):
    print(i)
# 2.  그냥 join 으로  출력 
print("\n".join("{}\t{}".format(k, v) for k, v in student.items()))
