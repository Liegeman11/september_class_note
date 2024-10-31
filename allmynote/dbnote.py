import mysql.connector as sql
# from decouple import config 

# my_con = sql.connect(host=config('host'), user=config('user'), passwd=config('passwd'))
myCon = sql.connect(host="127.0.0.1", username='root', passwd='Micheal@111', db= 'registrationdb')

myCursor = myCon.cursor()
# myCursor.execute("CREATE DATABASE registrationDb")
# myCursor.close()
# print('done')

# myCursor.execute("SHOW DATABASES ")
# for db in myCursor.fetchall():
#     print(db)
# myCursor.close()

# myCursor.execute("SHOW DATABASES ")
# for num, db in enumerate(myCursor):
#     print(num, '>>>',db)
# myCursor.close()
    
# myCursor.execute(" CREATE TABLE register(id INT(3) PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20), age INT(2), gender VARCHAR(6))")
# myCursor.close()
# print('done')


myCursor.execute("SHOW COLUMNs FROM register ")
for num, col in enumerate(myCursor):
    print(num, '>>>',col)
myCursor.close()

myCursor.execute(" ALTER TABLE register CHANGE id user_reg_id INT(3) AUTO_INCREMENT")
myCursor.close()
print('column renamed successfully')

# myCursor.execute(" ALTER TABLE register ADD email VARCHAR(50) UNIQUE")
# print('column renamed successfully')

# myCursor.execute(" ALTER TABLE register ADD contact VARCHAR(11) UNIQUE")
# myCursor.close()
# print('column renamed successfully')

# myCursor.execute(" ALTER TABLE register CHANGE email emails VARCHAR(50)")
# myCursor.close()
# print('column renamed successfully')

# my_query= "INSERT INTO register (name, age, gender, emails, contact) VALUES(%s,%s,%s,%s,%s)"
# user_info= ('tolu',24, 'female','tolu@gmail.com', '09012345678')
# myCursor.execute(my_query, user_info)
# myCon.commit()
# myCursor.close()
# print(f'{myCursor.rowcount} record inserted successfully')



import mysql.connector as sql

myCon = sql.connect(host='127.0.0.1', username='root', password='busolami2003@', db='registrationdb')

myCursor = myCon.cursor()
# myCursor.execute('CREATE DATABASE registrationdb')
# print('done')
# myCursor.close()
# myCursor.execute('SHOW DATABASES')
# for db in myCursor.fetchall():
#     print(db)
# myCursor.close()




# myCursor.execute('SHOW DATABASES')
# for num, db in enumerate(myCursor):
#     print(num,'>>>',db)
# myCursor.close()

# myCursor.execute('CREATE TABLE register(id INT(3) PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20), age INT(2), gender VARCHAR(6))')
# myCursor.close()
# print('done')

# myCursor.execute("SHOW COLUMNS FROM register")
# for num, db in enumerate(myCursor):
#     print(num,'>>>',db)
# myCursor.close()

# myCursor.execute('ALTER TABLE register CHANGE reg_id user_reg_id INT(3) AUTO_INCREMENT')
# myCursor.close()
# print('column renamed successfully')

# myCursor.execute("SHOW COLUMNS FROM register")
# for num, col in enumerate(myCursor):
#     print(num,'>>>',col)
# myCursor.close()

# myCursor.execute('ALTER TABLE register ADD email VARCHAR(50) UNIQUE')
# myCursor.close()
# print('column added successfully')

# myCursor.execute('ALTER TABLE register ADD contact VARCHAR(11) UNIQUE')
# print('column added successfully')

# myCursor.execute('ALTER TABLE register CHANGE email emails VARCHAR(50)')
# myCursor.close()
# print('column renamed successfully')

# myQuery = 'INSERT INTO register (name, age, gender, emails, contact) VALUES(%s,%s,%s,%s,%s)'
# user_info = ('tolu', 24, 'female', 'tolu@gmail.com', '09123456789')
# myCursor.execute(myQuery, user_info)
# myCon.commit()
# myCursor.close()
# print(f'{myCursor.rowcount} record inserted successfully')

# x = 0
# for each in range(0, 8):
#     name = input('Enter your name: ')
#     age = input('Enter your age: ')
#     gender = input('Type F for female or M for male: ')
#     emails = input('Enter your email: ')
#     contact = input('Enter your phone number: ')

#     myQuery = 'INSERT INTO register(name,age,gender,emails,contact) VALUES(%s,%s,%s,%s,%s)'
#     val = (name, age, gender, emails, contact)

#     try:
#         myCursor.execute(myQuery, val)
#         x+=1
#         myCon.commit()
#     except sql.Error as e:
#         print(f'Error: {e}')
# print(f'{x} row successfully inserted')

# myQuery = 'INSERT INTO register (name, age, gender, emails, contact) VALUES(%s,%s,%s,%s,%s)'
# user_info = (name, age, gender, emails, contact)

# myCursor.execute(myQuery, user_info)
# myCon.commit()
# myCursor.close()

# print(f'{myCursor.rowcount} record inserted successfully')

# myQuery ='SELECT * FROM register'
# myCursor.execute(myQuery)
# for each in myCursor.fetchall():
#     print(each)
# myCursor.close()

# myQuery ='SELECT * FROM register WHERE emails=%s'
# user_info = ('tj@gmail.com',)
# myCursor.execute(myQuery, user_info)
# for each in myCursor.fetchall():
#     print(each)
# myCursor.close()

# myQuery ='SELECT name, contact FROM register WHERE age=%s'
# val = (24,)
# myCursor.execute(myQuery, val)
# for each in myCursor.fetchall():
#     print(each)
# myCursor.close()

# myQuery ='SELECT name, contact FROM register'
# myCursor.execute(myQuery)
# for each in myCursor.fetchall():
#     print(each)
# myCursor.close()

# myQuery ='SELECT name, contact, age FROM register WHERE age>=15'
# val = (24,)
# myCursor.execute(myQuery)
# for each in myCursor.fetchall():
#     print(each)
# myCursor.close()

# TO UPDATE
# myQuery = "UPDATE register SET name ='julie' WHERE name=%s"
# val = ('kike',)
# myCursor.execute(myQuery, val)
# myCon.commit()
# print(f'1 record updated successfully')

# myQuery = "UPDATE register SET name ='tkristinimi', age ='17' WHERE emails=%s"
# val = ('tk@gmail.com',)
# myCursor.execute(myQuery, val)
# myCon.commit()
# print(f'1 record updated successfully')

# user = input('Enter your name>>> ')
# email = input('Enter your email>>> ')
# query = 'SELECT name, emails FROM register WHERE name=%s AND emails=%s'
# val = (user, email)
# myCursor.execute(query, val)
# user_info = myCursor.fetchone()
# if user_info:
#     print('access granted')
# else:
#     print('kindly register to be granted access')

#HOW TO DELETE
# query = "DELETE FROM register WHERE emails=%s"
# val = ('bimbo@gmail.com',)
# myCursor.execute(query, val)
# myCon.commit()
# print('1 record deleted successfully')