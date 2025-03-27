from todo_package.func import *

while True: #1.
    print("\n===== 📜 메뉴 =====")
    print("""
        1. 일정 추가
        2. 일정 확인
        3. 일정 완료
        4. 일정 삭제
        """)
    choice = input("메뉴 선택 : ")
    if choice == "1":
        add_todo()
    elif choice == "2":
        check_todo()
    elif choice == "3":
        complete_todo()
    elif choice == "4":
        delete_todo()
    else:
        print("다시 선택해 주세요.")
        continue