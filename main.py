class Student:
    nationality = "china"       # 定义成员属性填写的信息为默认信息

    # 没有声明的成员属性，在下面的的方法会重新声明
    def __init__(self, name, age, hobby):
        self.name = name         # 没有出现过的属性
        self.age = age           # 被重新声明
        self.hobby = hobby       # __init__方法中的代码， 创建对象就会全部执行
        print("姓名", self.name, "年龄", self.age, "爱好", self.hobby)

# 通过ctrl+p，查看方法可传入，需要传入的参数


stu_1 = Student("claire", 18, "music")

print(stu_1.nationality)


var_1: str = "你好"
print(var_1)
var_1 = var_1.upper()
print(var_1)

# 注解出现错误，有警告但不会报错
my_list: list[str] = [777, False]         # 出现警告，运行不报错
print(my_list[1], type(my_list[1]))


# 元组的注解必须逐一且完全正确
my_tuple: tuple[str, int, bool] = ("hello", 777, False)
print(my_tuple, type(my_tuple))


# 可以不遵循注解的要求，只要字典里面有一个符合要求就可以了
my_dict: dict[str, str] = {"hello": 777, "welcome": 555, 16: 85, "aa": "oo"}
print(my_dict)

a = 1        # type:int
b = True     # type:bool
print(b)

