# 数据类型
#    整数
#    浮点数
# ###########字符串
big_name = 'andy'
small_name = "tom"
family = "I'm ok"  # '本身也是一个字符，那就可以用""括起来
print(big_name, 'to', small_name, family)
especial_str = 'I\'m \"DASHENG\"!'  # 字符串内部既包含'又包含",用转义字符\
print(especial_str)

# \n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
# 用r''表示''内部的字符串默认不转义
print('\\\t\\')
print(r'\\\t\\')
# 用'''...'''的格式表示多行内容
print('line1\nline2\nline3')
print('''line1
line2
line3''')
# ###############

#    布尔值 True,False
print(4 > 3)  # True
# and\ or \not
#    空值 None


# 可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
variable = 'name'
print(variable)
print(isinstance(variable, str))  # True
variable = 16
print(variable)
print(isinstance(variable, int))  # True

# 常量  通常用全部大写的变量名表示常量
print(10 / 3)  # 3.3333333333333335
print(9 / 3)  # 3.0
print(9 // 2)  # 4 地板除
print(9 % 2)  # 1 余数
