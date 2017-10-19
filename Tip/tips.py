from collections import namedtuple

# 给元组命名
Student = namedtuple('student', ['name', 'age', 'sex', 'email'])

s1 = Student('mtianyan', 18, 'male', '1147727180@qq.com')
print(s1)
s2 = Student(name='mtianyan', age=18, sex='male', email='1147727180@qq.com')
print(s2)

print(s1.name)
print(s2.email)

print(isinstance(s1, tuple))
