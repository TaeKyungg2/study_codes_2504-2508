from sqlalchemy import text,create_engine

engine = create_engine("mysql+pymysql://root:1234@localhost:3306/mydb2",
                       pool_size=10,
                       max_overflow=5,
                       pool_recycle=3600
                       , echo=True, future=True)

# with engine.begin() as conn:
#     sql=text("""select empno, ename,sal from emp""")
#     result=conn.execute(sql)
#     for row in result.mappings().all():
#         print(row)

# with engine.connect() as conn:
#     result=conn.execute(text("""select empno,ename,sal 
#              from emp
#              where ename=:nameZZ"""),{"nameZZ":"smith"})
#     for row in result:
#         print(row)

# with engine.begin() as conn:
#     result=conn.execute(text("""select ifnull(max(empno),0)+1 from emp"""))
#     empno =result.all()[0][0]
#     sql=text("""insert into emp(empno,ename,sal) values(:empno,:ename,:sal)""")
#     conn.execute(sql,{"empno":empno,"ename":"이갑연"+str(empno),"sal":10000})

#     result=conn.execute(text("select * from emp"))
#     for row in result:
#         print(row)

with engine.begin() as conn: #use begin, go transaction.
    sql=text("insert into test1 values(:id,:field)")
    conn.execute(sql,{"id":12,"field":"Job"})

    sql=text("insert into test1 values(:id,:field)")
    conn.execute(sql,{"id":13,"field":"dongheasdfasdf"})