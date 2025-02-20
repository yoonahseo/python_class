name = "채현호"
age = 39.15
"제 이름은  ___ 입니다."
print("제 이름은" + name + "입니다.")
print("제 이름은", name, "입니다")
print("제 나이는", age ,"입니다")

print("제 나이는 {} 이고 이름은 {}입니다.".format(age, name))

print("제 나이는 {a} 이고 이름은 {b}입니다.".format(a=39, b="채현호"))
print(f"제 나이는 {age} 이고 이름은 {name}입니다.")
print("제 나이은 %s 입니다." % age) # 문자열로 들어간다.
print("제 나이는 %d 입니다." % age) # 모든 숫자가 정수로 들어간다.
print(f"제 나이는 %d 이고 이름은 %s 입니다." %(age, name)) #f포맷 %d 정수 %s 문자열

