import pymysql as pmy

connection=pmy.connect(
  host='localhost',
  user='root',
  password='qwerty123',
  database='trial'
)

# if(connection):
#     print("Successfully connected to the database")