#싱속

# class Parent:
#     def intoduce(self):
#         print("저는 부모입니다")
# class Child(Parent):
#     def intoduce(self):
#         print("저는 자식입니다.")
# Child = Child()
# Child.intoduce()


# class Car:
#    def __init__(self,model,price):
#        self.model = model
#        self.price = price
#    def drive(self):
#        print(f"{self.model}가 앞으로 전진합니다")
# class ElecCar(Car):
     def __init__(self,model,price,energy_efficency):
#         super().__init__(model,price)
#         self.energy_efficiency = energy_efficency
#     def drive(self):
#         super().drive()
#         print(f"{self.model}이 전기로 전진합니다")
#
# ev6 = ElecCar("ev6","5000","60kwh")
# ev6.drive()

# 다중상속

# class Father:
#     def drive(self):
#         print("운전을 잘함")
# class Mother:
#     def cook(self):
#         print("요리를 잘함")
# class Child(Father, Mother):
#     def Study(self):
#         print("공부를 잘함")

# class Animal:
#     def breathe(self):
#         print("숨을 쉴 수 있어요")
# class Swimmer:
#     def swim(self):
#         print("헤엄을 칠수 있어요")

# class GrandParent:
#     def smart(self):
#         print("똑똑해요")
# class Father(GrandParent):
#     def doctor(self):
#         print("나는 의사")
# class Mother:
#     def rich(self):
#         print("나는 부자")

# class A:
#     def introduce(self):
#         print("나는 A")
# class B:
#     def introduce(self):
#         print("나는 B")
# class C:
#     def introduce(self):
#         print("나는 C")
#
# class Child(A,B,C):
#     def introduce(self):
#         print(Child.mro())
#         super().introduce()
#         super(A,self) .introduce()
#         C.introduce()
# child = Child()
# child.introduce()

#MRO Method Resolution 호출순서

class Car:
    def __init__(self,brand,model):
     self.brand = brand
     self.model = model

class ElectricCar(Car):
    def __init__(self,brand,model,battery_capacity):
     super().__init__(brand,model)
     self.battery_capacity = battery_capacity
    def charge(self):
        print(f"{self.brand}의 {self.model}가 배터리를 충전합니다")


class GasolineCar(Car):
    def __init__(self,brand,model,fuel_tank_capacity):
     super().__init__(brand,model)
    def refuel(self):
     print("f"{self.brand}의 {self.model}가 연료를 주유합니다.")

class Person:
    def __init__(self,age,emai):








