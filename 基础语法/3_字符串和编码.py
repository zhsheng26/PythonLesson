# ord()函数获取字符的整数表示
print(ord('A'))  # 65
# chr()函数把编码转换为对应的字符
print(chr(66))  # B
print('\u4e2d\u6587')
# 对bytes类型的数据用带b前缀的单引号或双引号表示：
print(b'ABC'.decode('ascii'))
# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 用len()函数,计算str包含多少个字符
print('"中国"的字符长度：', len('中国'))
# 换成bytes，len()函数就计算字节数
encode_char = '中文'.encode('utf-8')
print(encode_char)  # b'\xe4\xb8\xad\xe6\x96\x87'
print(len(encode_char))

# 字符串格式化

print('Hi, %s, you have $%d.' % ('Michael', 1000000))
# %d 整数
# %f 浮点数
# %x 十六进制整数
# %s 字符串


# 格式化整数和浮点数可以指定是否补0和整数与小数的位数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
# %s会把任何数据类型转换为字符串：
print('Age: %s. Gender: %s' % (25, True))
# 用%%来表示一个%：
print('growth rate: %d %%' % 7)
