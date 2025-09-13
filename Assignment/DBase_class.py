import pymysql as pyms
# pip install python-decouple
# from decouple import config
my_con = pyms.connect(host= config('host'), user= config('user'), passwd= config('passwd'),)

print(my_con)
print('connection successful')