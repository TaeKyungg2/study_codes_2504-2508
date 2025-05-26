import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    password='rudxorhkr',
    db='mydb',
    port=3306
)

cursor=conn.cursor(pymysql.cursors.DictCursor)
ename='SCOTT'
sql="select * from emp where ename='"+ename+"' "
print(sql)
cursor.execute(sql)
rows=cursor.fetchall()
print("datacount:",len(rows))
for row in rows:
    print(row["empno"],row["ename"],row["sal"])

sql="""
     insert into emp(empno,ename,sal)
     values(%s,%s,%s)
"""
#cursor.execute(sql,(9000,'백승빈',6000))
conn.commit() #connect instance should be committed to save changes

sql="select ifnull(max(empno),0)+1 id from emp"
cursor.execute(sql)
row=cursor.fetchone()
print(row)
sql="""
     insert into emp(empno,ename,sal)
     values(%s,%s,%s)
"""
cursor.execute (sql,(row['id'],'백승빈',6000))

conn.commit() #connect instance should be committed to save changes

conn.close()

