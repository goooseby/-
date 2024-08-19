class MyClass:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        print("学生")


for i in range(1, 4):
    print(f"当前录入第{i}位学生信息， 共需要录入3位学生")
    stu = MyClass(input("姓名"), int(input("年龄")), input("地址"))
    print(f"学生{i}信息录入成功， 姓名{stu.name}， 年龄{stu.age}， 地址{stu.address}")

