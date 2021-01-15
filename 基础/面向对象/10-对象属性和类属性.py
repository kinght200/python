class Person(object):
    type = '人类'  # 这个属性定义在类里，函数之外，我们称之为类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 对象p 是通过Person 类创建出来的实例对象
# name 和 age 是对象属性，在 __init__ 方法里，以参数的形式定义的
# 每一个实例对象都会单独保存一份的属性
# 每个实例对象之间的属性没有关联，互不影响
p1 = Person('张三', 18)
p2 = Person('李四', 19)

x = p1
print(p1.name)
print(x.name)

# 类属性可以通过类对象和实例对象获取
print(Person.type)  # 可以通过类对象获取类属性

# 可以通过实例对象获取类属性
print(p1.type)
print(p2.type)

# 类属性只能通过类对象来修改，实例对象无法修改类属性
p1.type = 'human'
print(p1.type)  # 并不会修改类属性，而是给实例对象添加了一个新的对象属性

Person.type = 'monkey'  # 修改了类属性
print(p2.type)  # monkey
print(p1.type)  # human

# 获取两个对象的内存地址 0x27098285FD0 0x27098285F10
# print('0x%X 0x%X' % (id(p1), id(p2)))
