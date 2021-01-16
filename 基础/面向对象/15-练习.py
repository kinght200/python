# 定义一个类属性，记录通过这个类创建了多少个对象

class Person(object):
    __count = 0

    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        return object.__new__(cls)  # 申请内存，创建一个对象，并设置类型是 Person 类

    def __init__(self, name, age):
        Person.__count += 1
        self.name = name
        self.age = age


# 每次创建对象，都会调用__new__ 和 __init__ 方法
# 调用 __new__ 方法，用来申请内存
# 如果不重写 __new__ 方法，它会自动找 object的 __new__ 方法
# object的 __new__ 方法，默认是实现申请了一段内存，创建了一个对象
p1 = Person('张三', 19)
p2 = Person('李四', 18)
p3 = Person('jack', 20)
# print(Person.count)

print(p1, p2, p3)

# 申请了内存，创建了一个对象，并设置它的类型是Person
p4 = object.__new__(Person)
p4.__init__('tony', 23)
print(p4.name, p4.age)
