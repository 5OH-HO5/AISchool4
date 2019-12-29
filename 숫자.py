# 변수에 숫자넣기
a = 3
print(a)

b = 1
print(b)

# 같은 변수명이라면 최근 저장한 값으로 반환
a = 12
print(a)

# 지수표기법
a = 3.5e-3
print(a)
# 0.0035

a = 2e+3
print(a)
# 2000.0

# 형 변환

a = 3.7
print(a)
b = int(a)
print(b)
# int = 정수형 / float = 실수형

# 자료형 확인
print(float(b))
print(type(a))
print(type(b))

a = 3
b = 6
c = a + b
print(a + b)
print(c)
print(a - b)
print(a*b)
print(int(a/b))
# print 내에서 정의된 변수를 더하거나 더한 변수를 정의해줘도 값은 같다
# 덧+ 뺼- 곱* 나/
# 정수형 + 실수 = 실수

a = 5
b = 2
print(a ** b)
# **는 제곱

print(a % b)
# %는 나머지

print(a//b)
# //는 몫

# 평균 예제
a = 90
b = 60
c = 81
average = (a + b + c) / 3
print(average)