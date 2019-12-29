# 문자열(String)
print("Hello World")
print('Hello World')

print("a")
print("123", "456")
print("456")
print("123", end=" ")
print("111")
# end라는 parameter 넣는다 //  \n은 줄바꿈 // \t는 tap

c = "ohminjae's paper"
print(c)

# 작은따옴표 안에 작은따옴표 쓰고 싶을 때 \
e = 'ohminjae\'s paper'
print(e)

# 큰 따옴표 앞에 \
d = 'He said "Hi"'
print(d)

f = "He said \"Hi\""
print(f)

# \n 행바꿈 // 계획문자
multiline = "Life is too short \nYou need python"
print(multiline)

multiline = "Life is too short \n\nYou need python"
print(multiline)

# """ 큰 따옴표 3개를 문장의 첫번째와 마지막에 쓰면 워드처럼 쓸 수 있다.
ex = """
Life is too short

You need python
"""
print(ex)

# 문자열 연산
teacher = "Kangmin's "
title = "AI School"
print(teacher + title)

print("="*30)
print(teacher + title)
print("="*30)

print((teacher + title) * 2)

# 문자의 갯수를 출력
print(len(title))
print(len(teacher))

# 문자열 인덱싱 // []안에 index 번호
print(title[0])
print(title[1])
print(title[3])

# []안에 - 붙이면 뒤에서부터 번호
print(title[-1])
print(title[-2])

# 문자열 슬라이싱 // [번호 : 번호]는 범위
print(title[0:3])
print(title[3:])
print(title[:7])

odd_even = "홀짝홀짝홀짝"
print(odd_even[::2])
print(odd_even[1::2])

# 문자열 관련 함수
a = "apple"
print(a.count("p"))
# count(parameter) = 문자열에 parameter가 몇 개 있는지 찾아준다

print(a.find("p"))
# find(parameter) = 문자열에 parameter가 몇번째에 있는지 찾아준다

print(a.index("p"))
# index와 find의 차이점? // apple에서 없는 글자 t를 검색하면
# index는 에러 출력
# find는 -1 출력

print(".".join(a))
# 문자열 하나하나에 반영해준다

# 대문자로
a = a.upper()
print(a)

# 소문자로
print(a.lower())

num = "234"
print(num)
num = float(num)
print(num)

num = str(num)
print(num)

b = " How can I improve my coding skills? "
print(b)

# 좌우에 공백데이터를 벗겨낸다
b = b.strip()
print(b)

b = b.replace("?", "")
print(b)

word_list = b.split(" ")
print(word_list)

# 문자열 포매팅
apple_num = 4
orange_num =2
apple_num_string = "three"
print("I eat %d apples." % apple_num)
print("I eat {} apples.".format(apple_num))
print("I eat %s apples." % apple_num_string)
print("I eat %d apples and %d oranges." % (apple_num, orange_num))
# {}안에 index 번호로 원하는 값 출력 가능
print("I eat {} apples and {} oranges.".format(apple_num, orange_num))

print(f"I eat {apple_num} apples and {orange_num} oranges.")

print("Error is %d%%." %97)

pi = 3.141592
print("pi = %f" % pi)
print("pi = %0.4f" % pi)

# 연습문제
print("Mary's cosmetics")
print(len("dk2jd923i1jdk2jd93jfd92"))
t1 = 'python'
t2 = 'java'
print((t1 + t2) * 3)
id = "890910-1157963"
print(id[:2])
license_plate = "24가 2210"
print(license_plate[-4:])
url = "portal.ac.kr"
url_list = url.split(".")
print(url_list[-1])