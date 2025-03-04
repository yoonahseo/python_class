import random
choice_list =["가위","바위","보"]
user_choice = ""
computer_choice =""
use_score = 0
computer_score = 0

while True:
    if "user_score" == 5:
        print("사용자 승리~!!!!")
        break
    elif "comouter_score" == 5:
        print("컴퓨터 승리~!!!!")
    user_choice = input("가위,바위,보 중 선택해 주세요:")

    if user_choice not in choice_list and user_choice != "종료":
        print("가위, 바위, 보 중 다시 선택해 주세요")


    computer_choice =random.choice(choice_list)

    if user_choice == computer_choice:
        print("무승부 입니다")

    elif (user_choice == "가위" and computer_choice == "보") or\
         (user_choice == "바위"  and computer_choice == "가위")or\
         (user_choice == "보" and computer_choice == "바위"):
        print("이겼습니다!!!")
        use_score +=1

    else:
        print("졌습니다 ㅜㅜ")

