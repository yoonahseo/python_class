# def func1():
#     print("hello world")
#
# def plus():
#     a = 2
#     b = 3
#     print(a + b)
# 매개변수가 있는 사용자 정의함수
# def hello(name):
#       print(f"안녕하세요 저는 {name}입니다.")
#       hello("홍길동")
from operator import ifloordiv

# def plus(x, y):
#     print(x + y)
#     plus(5, 6)

# def introduce(name,age):
#    print(f"제 이름은 {name}이고 나이는 {age}입니다.")
#    introduce(age=27, name="이동윤")
# 리턴값이 있는 사용자 정의 함수

# def plus(x, y):
#     return x + y
#
# result=plus(1,2)
# print(result)
# print(plus(1,2))

# def check_divide_seven(num):
#     if num % 7 == 0:
#         return True
#     else:
#         return False
# def factorial(num):
#     sum = 1
#
#     for n in range(num) :
# print(f"n={n}")
#     sum = sum * (n+1)
# print(f" sum ={sum}")
#     return sum
# print(factorial(7))

#1. 두수의 입력받고 두수의 합을 출력하는 함수



# def cal_average(scores):
#     sum = 0
#     for score in scores:
#         sum += score
#     return sum/len(scores)
# score_list1 = [55, 70, 100]
# score_list2 = [100, 99, 88]
# score_list3 = [80, 70, 60]
#
# print(cal_average(score_list1))
# print(cal_average(score_list2))
# print(cal_average(score_list3))

#콜백함수
# import time
# def timer(pause_second, callback):
#     print(f"{pause_second}초 타이머가 시작되었습니다")
#     print(f"{pause_second}초 뒤에 함수가 실행됩니다.")
#
#     time.sleep(pause_second)
#
#     callback()
# print("타이머가 종료되었습니다")
#
# def hello():
#     print("안녕")
# timer(5, hello)
# lamda함수(익명함수, 미시 함수)
#

# #lamda 매개변수1, 매개변수2,...함수 내부 코드
# def plus(x, y):
#     return x + Y
# print(plus(4, 5))
#
# add_lambda = lambda x, y: x + y
# print(add_lambda(4, 5))

num = int(input("숫자:"))

# def parity(a):
# if num % 2 == 0:
#     print("짝수")
# else:
#     (print("홀수")
# parity(a)




