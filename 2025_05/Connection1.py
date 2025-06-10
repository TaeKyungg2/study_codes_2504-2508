#pip install sqlalchemy 
#버전 2.0이상 
#C:\Users\littl\AppData\Roaming\Python\Python38\site-packages\sqlalchemy
#https://soogoonsoogoonpythonists.github.io/sqlalchemy-for-pythonist/tutorial/1.%20%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC%20%EA%B0%9C%EC%9A%94.html#%E1%84%8C%E1%85%A6%E1%84%80%E1%85%A9%E1%86%BC%E1%84%83%E1%85%AC%E1%84%82%E1%85%B3%E1%86%AB-%E1%84%80%E1%85%A5%E1%86%BA

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# SQLAlchemy가 PyMySQL을 내부적으로 사용하며 pool 지원
engine = create_engine(
    "mysql+pymysql://root:rudxorhkr@localhost/mydb",
    pool_size=10,         # 최대 연결 수
    max_overflow=5,       # 초과 시 추가 연결 수
    pool_recycle=3600     # 재활용 시간
)

try:
    conn = engine.connect()
    print("데이터베이스 연결 성공") #연결 객체를 얻는다.
except SQLAlchemyError as e:
    print("데이터베이스 연결 실패:", e)


#2.0 이전 버전 conn.execute("쿼리")
result = conn.execute(text("SELECT * FROM emp"))
# for row in result:
#     print(row)

#dicttype 으로 출력
rows = result.mappings().all()
for row in rows:
        print(dict(row))
conn.close()

#데이터추가하기
conn = engine.connect() 
sql = text("""
    insert into emp (empno, ename, sal )
    values(:empno, :ename, :sal) 
""")
conn.execute( sql, [{"empno":10001, 
                        "ename":"우즈2", 
                        "sal":8000}, 
                        {"empno":10002, 
                        "ename":"우즈3", 
                        "sal":8000}] )
conn.commit() 
conn.close() 