# 变量从内存中变成可存储或传输的过程称之为序列化
# pickling和unpickling
import json
import pickle

# pickle.dumps()方法把任意对象序列化成一个bytes

stu_dict = dict(name='andy', age=12, score=90)
pick_write = pickle.dumps(stu_dict)
print(pick_write)

file_pick = open('pickling_obj.txt', 'wb')
with file_pick as f:
    pickle.dump(stu_dict, f)

pick_read = open('pickling_obj.txt', 'rb')
with pick_read as re:
    pickle_load = pickle.load(re)
    print(pickle_load)
    print(type(pickle_load))
# json序列化
json_dump = json.dumps(stu_dict)
print(json_dump)
pick_write_json = open('pickling_json.txt', 'w')
with pick_write_json as wj:
    json.dump(stu_dict, wj)
    json.dump(json_dump, wj)
# json反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(type(json.loads(json_str)))


# json进阶

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
