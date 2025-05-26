import pymysql
from datetime import datetime
def Connection(func):
    def inner(*ags,**kwargs):
        conn=pymysql.connect(
        host='localhost',
        user='root',
        password='rudxorhkr',
        db='mydb',
        port=3306)
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        func(cursor,*ags,**kwargs)
        conn.commit()
        conn.close()
        return 
    return inner

class student():
    sname=None
    korScore=None
    engScore=None
    mathScore=None
    regdate=None
    @Connection
    @classmethod
    def add(cls,conn):
        cls.sname=input("Enter your name: ")
        cls.korScore=input("Enter your score: ")
        cls.engScore=input("Enter your score: ")
        cls.mathScore=input("Enter your score: ")
        cls.regdate=datetime
        conn.execute(
            """insert into score(sname,korScore,engScore,mathScore,regdate)
            values(%s,%s,%s,%s,%s)""",
            (cls.sname,cls.korScore,cls.engScore,cls.mathScore,cls.regdate))
        print("Student added successfully!")
    
    @Connection
    @classmethod
    def modify(cls,conn):
        cls.sname=input("Enter your name: ")
        cls.korScore=input("Enter your score: ")
        cls.engScore=input("Enter your score: ")
        cls.mathScore=input("Enter your score: ")
        sql="""update score set sname=%s
        , korScore=%s, engScore=%s, mathScore=%s 
        where sname=%s"""
        conn.execute(sql,(cls.sname,cls.KorScore,cls.engScore,cls.mathScore,cls.sname))
    @Connection
    def delete(conn):
        cls.sname=input("Enter your name: ")
        sql="delete from score where sname=%s"
        name=input("Enter your name to delete: ")
        conn.execute(sql,(name))
    def select(conn):
        id=input("Enter see your id: ")
        conn.execute("select * from tb_score where sname=%s", (id))
        row=conn.fetchone()
        print(row)
    
    @Connection
    def allprint(conn):
        sql='select * from tb_score'
        conn.exercute(sql)

class manager():
    def main():
        funList=[None,None,cls.modify,cls.delete,cls.select,cls.allprint]
        while True:
            print("1. Add Student")
            print("2. Modify Student")
            print("3. Delete Student")
            print("4. Select Student")
            print("5. Print All Students")
            print("6. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                stu=cls()
                stu.add()
            elif choice >= 2 and choice <= 5:
                funList[choice-1]()
            elif choice == 6:
                return
            else:
                print("Invalid choice, please try again.")
manager.main()