import json
import time

def save_todo(todo_list):
    with open("todo.json", "w") as new_file:
        json.dump(todo_list, new_file, indent=4, ensure_ascii=False)

    print("저장되었습니다.")


def add_todo():
    with open("todo.json", "r", encoding="utf-8") as file:
        todo_list = list(json.load(file))
    while True:
        todo_name = input("해야할 일(그만하려면 종료) : ")
        todo_complete = False
        if todo_name == "종료":
            save_todo(todo_list)
            break

        todo_list.append({"todo_name": todo_name, "todo_complete": todo_complete})

def hgj (sentence, timesl=0.05):
    for i in range(len(sentence)):
        print(sentence[i], end="")
        time.sleep(timesl)

def check_todo():
    with open("todo.json", "r", encoding="utf-8") as file:
        todo_list = list(json.load(file))

    for i in range(0, len(todo_list)):
        str = f"{i + 1}. 해야할 일 : {todo_list[i]["todo_name"]} 완료상태 : {"O" if todo_list[i]["todo_complete"] == True else "X"} \n"
        hgj(str)

    return todo_list

def complete_todo():
    todo_list = check_todo()
    while True:
        choise_todo = int(input("몇 번째 ToDo를 완료 하시겠습니까?"))
        todo_list[choise_todo - 1]["todo_complete"] = True

        input_str = input("또 완료하시겠습니까? y/n")
        if input_str.lower() == "y":
            continue
        else:
            with open("todo.json", "w") as new_file:
                json.dump(todo_list, new_file, indent=4, ensure_ascii=False)
            break

def delete_todo():
    todo_list = check_todo()

    choise_todo = int(input("몇 번째 ToDo를 삭제 하시겠습니까?"))
    del todo_list[choise_todo - 1]

    with open("todo.json", "w") as new_file:
        json.dump(todo_list, new_file, indent=4, ensure_ascii=False)