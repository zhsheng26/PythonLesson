from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///./time.db', echo=True)  # 定义引擎
meta_data = MetaData(engine)

user_table = Table('user', meta_data,
                   Column('id', Integer, primary_key=True),
                   Column('name', String),
                   Column('email', String))
user_table.create()
table_insert = user_table.insert()
table_insert.execute(name='rsj217', email='rsj21@gmail.com')
table_insert.execute({'name': 'ghost'}, {'name': 'test'})
