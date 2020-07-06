"""
input: 0; CREATE TABLE devs (name VARCHAR(128)); -- 
ниже вместо 11012001 должен стоять Ваш пароль для входа в клиент MySQL
"""


import MySQLdb
id = input("Enter colour id...")
sql = 'SELECT colour FROM colours WHERE colour_id= '+ id +''
print(sql)

conn = MySQLdb.connect('localhost', 'root', '11012001', 'colours')
cursor = conn.cursor()
 
cursor.execute(sql)
 
# Получаем данные.
row = cursor.fetchone()
print(row)
 
# Разрываем подключение.
conn.close()
