


#abs()
#숫자의 절대값을 리턴하는 함수
print(abs(-10))
print(abs(-1.2))

#all()
#all(X)는 반복 가능한 데이터 x를 입력값으로 받으면 X의 요소가 모두가 참이면 ,거짓이 하나라도 있으면 FALSE를 리턴

num_list = [1, 2, 0, 4]
print(all(num_list))
num_list = []
print(all(num_list))

#any
#그냥 all()의 반대 X의 요소가 하나라도 참이면 , ㅈ거짓이 하나라도 있으면 FALSE를 리턴

#chr()
#chr(i)는 유니코드를 넣으면 해당문자로 리턴

print(chr(97))
print(chr(44032))

#dir()
#객체가 지닌 변수난 함수를 보여주는 함수
#name = "python"
#print(dir(name))

#divimod()
#2개의 숫자 a,b를 입력받고 그리고 a를 b로나눈 몫과 나머지를 튜플 형태로 리턴
#print(divmod(7,3))
#enumerate()
#
# a_list = ["name", "age", "birth"]
# for i, name in enumerate(a_list):
# print(i,name)

#filter()
#첫 번째 인수로 함수, 두번째 인수로 반복 가능한 데이터
#그리고 빈복 가능한 데이터의 요소 순서대로 함수를 호출
#리턴값이 참인것만 묶어서 리턴

# def positive(x):
#     return x > 0
#
# print(list(filter(positive, [1, -2, 5, -3, 8])))

#age = int(input("몇살입니까?>>>"))
# if age <= 7:
#     print("미취학")
# elif age <=

#hex()
#정수를 입력받아 16진수 문자열로 변환하여 리턴하는 함수
# print(hex(234))
# print(hex(3))
# a = 3
# print(id(3))
#map()
#map은
# def two_time(x):
#     return x*2
#
# print(list(map(two_time,[1,2,3,4])))
#max()
#반복가능한 데이터 중에서 최대값 리턴
# num_list =[1, 3, 13, 20, 18, 17, 5, 9]
#print(max(num_list))
#print(min(num_list))

#oct()
#oct()는 정수를 8진수 문자열로 바꾸어 리턴하는 함수
#print(oct(34))

#open()
#open(filename, [model] "파일이름"과"읽기 방법"을 입력받아 파일 객체를 리턴
# w 쓰기모드
# r 읽기모드
# a 추가모드
# b 바이너리 모드

# file = open("example.txt", "r",encoding="utf_8")
# print(file)
# content = file.read()
# print(content)
# file.close()

# with open ("example.txt", "r",encoding="utf_8") as file:
#     content = file.read()
#     print(content)
# **중요-
#ord()
# print(ord("가"))

#pow()
#첫번째 인수의 두번째 인수만큼 거듭제곱 한값을 리턴

#range()
#range(시작, 끝, 간격)for 문과 함께 자주 사용
#이 함수는  입력받은 숫자에 해당하는 범위 값을 반복가능한 객체로 만들어 리턴


# print(list(range(5,100,5)))
# print(round(4.4))
# print(round(8.9))
# print(round(5.1234,2))

#sum()
# 합계임
# num_list = [1234, 582, 1475, 55752]
# print(sum(num_list))








