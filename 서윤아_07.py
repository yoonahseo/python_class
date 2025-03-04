import random
#난이도 선택 유호성 검사를 위한 난이도 리스트
difficulty_list = ["쉬움","보통", "어려움"]
try_count = 0
correct_answer = random.randint(1,100)
guess = 0

while True:
    difficulty = input("난이도를 선택해 주세요(쉬움,보통,어려움")
    if difficulty in difficulty_list:
        break
    else:
        print("난이도를 다시 선택해 주세요")
        continue

if difficulty == "쉬움":
    max_try_count = 10
    max_range = 50
elif difficulty =="보통":
    max_try_count = 7
    max_range = 70
else:
    max_try_count = 5
    max_range = 100

correct_answer = random.randint(1,max_range)
print(f"선택된 난이도-{difficulty} 렌덤범위~{max_range} 최대시도횟수")
while  True:
    if try_count == max_try_count:
        print("최대 시도 횟수에 도달했습니다. 게임 종료")
        break

    input_str = input("숫자를 입력해 주세요:")

    if input_str.isdigit():
        guess = int(input("숫자를 입력해 주세요!!!"))
    else:
        print("숫자를 입력해 주세요!!")
        continue


    if correct_answer  >  guess:
        print("UP")
        try_count += 1
        print(f"시도횟수 : {try_count}")
    elif correct_answer < guess:
        print("DOWN")
        try_count += 1
    else:
        print("정답입니다!! 정답 : {correct_answer}")
        break
