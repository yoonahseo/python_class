# profile={
#     "name":"서윤아",
#      "age":56,
#      "hobby":["수영""요리"]
#  }
# print(profile[2])
#
#
# profile["job"]="백수"
# print(profile["job"])
# key_list = list(profile.keys())
# key_list.append("job")


# value_list=list(profile.values())
 #print(value_list)
# profile.items()
# item_list=list(profile.items())
# item_list.append(("job","백수"))
# print(item_list)

#python_grade= {
   # "윤아" : "B",
   # "길동" : "C",
   # "준식" : "A",
   # "상혁" : "D"
#}
# print(sorted(python_grade.items(), reverse=True))
#
# print(sorted(python_grade.items(),key=lambda  x: x[1]))
# print(sorted(python_grade.items(),key=lambda  x: x[1],reverse=True))

#student = {
#    "name":input("이름:"),
#     "score":int(input("점수:"))
# }
 #print(student)

# student = {
#     "name":"서윤아",
#     "score": 80
# }

# print(profile["student"])


# fruits={"사과","딸기","귤"}
# print(fruits)
#
# apple_str=set("apple")
# print(apple_str)

num = {1,2,5,5,6,8}
 #num.add(8)
 #print(num)
 # num.remove(1)
 # print(num)
 # num.update([10,11,12])
 #  print(num)
 # empty_set=set()#빈 세트

# num.discard(19)#오류안냄
# print(num)
#
# num.clear()
# print(num)

# a = {1, 2, 3, 4,5}
# b = {4, 5, 6, 7,8}
#
# print(a.union(b))
# print(a|b)
#
# print(a.intersection(b))
# print(a&b)
#
# print(a.difference(b))
# print(a - b)
#
# color = {"b","l","u","e"}
# print(color.pop())
# print(num)

# a = [21, 22, 23,25,26]
# b=  [22, 24, 27]
# common = set(a)&set(b)
# print(common)

python_class = ["수현","현호", "지니", " 가인"]
java_class = ["현호", "지니","홍수","찬호"]
common= set(python_class) & set(java_class)
print(common)

java=set(python_class)-set(java_class)
print(java)





