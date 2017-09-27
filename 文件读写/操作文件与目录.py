import os

print(os.name)
print(os.uname())

print(os.environ)
print(os.environ.get('PYTHONPATH'))
print(os.environ.get('x', 'default'))

current_dir = os.path.abspath('.')

path_join = os.path.join(current_dir, '操作文件与目录.py')
print(path_join)

path_split = os.path.split(path_join)  # ('I:\\PythonLesson\\进程和线程', '操作文件与目录.py')
print(path_split[0])

dir_list = [x for x in os.listdir('.') if not os.path.isdir(x)]
print(dir_list)
py_file = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(py_file)
