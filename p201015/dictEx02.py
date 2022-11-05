#dc= {'name': '홍길동', 5:'다섯' }
dc= {'name': '홍길동', 5:'다섯', 'even':[2,4,6,8] }

print('dc >>', dc)
#다섯 값 추출하기 
print('값 추출 >> ', dc[5])
#   sometihng[5]  >> 이 형태만 보고 리스트, 인덱스라고 앞서가선 안된다!! 

print('값 추출 >> ', dc.get(5))
#print('값 추출 >> ', dc.items()[0])# is not subscriptable 
print('값 추출 >> ', dc.items())

# even 키로 접근해여 리스트 값 추출 
print('리스트 값 추출 >>', type(dc['even']))

print("\n".join("{}\t{}".format(k, v) for k, v in sorted(dc.items(), key=lambda t: str(t[0]))))
print(sorted(dc.items(), key=lambda aaaaaaa: str(aaaaaaa[0])))
print('리스트의 마지막요소 추출 >> ', dc['even'][-1])

#d이름추출
print('name >>' ,dc['name'])
print(f'name >> {type(dc["even"][:-1])}')
print(f'name >> {dc["even"][:-1]}')
print(f'name >> {dc["even"][::-2]}')

