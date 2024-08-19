class AC:        # 接口（抽象类）
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def auto_wind(self):
        pass


"""
抽象类相当于模板， 
子类继承，都根据这个模板来的
子类中也能添加东西
"""


class GreeAc(AC):          # 继承抽象类， 定义具体的方法
    name = "Tom"

    def cool_wind(self):       # 接口的方法在子类中已经被复写
        print("格力制冷科技")

    def hot_wind(self):
        print("格力炙热科技")   # 没有复写auto_wind 功能，代码没有问题


class MideaAc(AC):           # 继承抽象类，采用独家科技

    def cool_wind(self):    # 复写方法
        print("美的制冷科技")

    def hot_wind(self):
        print("美的炙热科技")

    def auto_wind(self):
        print("美的自动科技")


"""
在以下函数中，使用同一种抽象的方法
传入不同的参数，得到不同的形态------->>>多态
实际上，可以不用抽象类
不用抽象方法，代码也能运行

"""


def make_cold(ac: AC):     # 定义函数，输入的参数为AC？
    ac.cool_wind()         # 输入参数不同，采用了不同的子类


def make_hot(ac: AC):      # 多态，参数的不同使得结果呈现多种状态
    ac.hot_wind()


def make_auto_wind(ac: AC):
    ac.auto_wind()


"创建类对象"

meidi = MideaAc()   # 创建类对象
geli = GreeAc()

"调用了函数，函数中采用了一种方法"
make_cold(meidi)
make_cold(geli)


make_hot(meidi)
make_hot(geli)

make_auto_wind(meidi)
make_auto_wind(geli)
print()
print()
meidi.auto_wind()
meidi.cool_wind()
print("为什么不直接使用类的方法，却要用多态")
