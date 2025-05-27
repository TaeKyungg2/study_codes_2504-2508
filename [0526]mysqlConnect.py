# conda activate myenv1
#pip intall pymysql
import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    password='rudxorhkr',
    db='mydb',
    port=3306
)

cursor=conn.cursor()
#through cursor we can execute sql queries
print("Connected to MySQL database successfully!")
sql="select * from emp"
cursor.execute(sql)
rows=cursor.fetchall()
# for row in rows:
#     print(type(row),row)


print("get one")
sql="select * from emp where empno=7369"
cursor.execute(sql)
row=cursor.fetchone()
print(row)

print("get 3")
sql='select * from emp where empno<8000'
rows=cursor.fetchmany(3)
for row in rows:
    print(row)

#get dict type
cursor=conn.cursor(pymysql.cursors.DictCursor)
conn.close()
