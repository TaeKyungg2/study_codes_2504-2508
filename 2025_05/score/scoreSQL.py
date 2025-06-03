from scoreDBModule import Database
from datetime import datetime

class student():
    sname=None
    kor=None
    eng=None
    mat=None
    regdate=None
    
    @classmethod
    @Database.Connection
    def add(cls,db):
        cls.sname=input("Enter your name: ")
        cls.kor=input("Enter your kor score: ")
        cls.eng=input("Enter your eng score: ")
        cls.mat=input("Enter your math score: ")
        cls.regdate=datetime.now()
        db.execute(
            """insert into tb_score(sname,kor,eng,mat,regdate)
            values(%s,%s,%s,%s,%s)""",
            (cls.sname,cls.kor,cls.eng,cls.mat,cls.regdate))
        print("Student added successfully!")

    @classmethod
    @Database.Connection
    def modify(cls,db):
        cls.sname=input("Enter your name: ")
        cls.kor=input("Enter your score: ")
        cls.eng=input("Enter your score: ")
        cls.mat=input("Enter your score: ")
        sql="""update tb_score set sname=%s
        , kor=%s, eng=%s, mat=%s 
        where sname=%s"""
        db.execute(sql,(cls.sname,cls.kor,cls.eng,cls.mat,cls.sname))
        print("Student modified successfully!")

    @classmethod
    @Database.Connection
    def delete(cls,db):
        sql="delete from tb_score where sname=%s"
        name=input("Enter your name to delete: ")
        db.execute(sql,(name))
        print("Student deleted successfully!")
    
    @classmethod
    @Database.Connection
    def select(cls,db):
        id=input("Enter see your id: ")
        row=db.executeOne("select *from tb_score where sname=%s", (id))
        print(row)

    @classmethod
    @Database.Connection
    def allprint(cls,db):
        sql='select * from tb_score'
        rows=db.executeAll(sql)
        for row in rows:
            print(row)

class manager():
    @classmethod
    def main(cls):
        funList=[None ,student.add,student.modify,student.delete,student.select,student.allprint]
        while True:
            print("1. Add Student")
            print("2. Modify Student")
            print("3. Delete Student")
            print("4. Select Student")
            print("5. Print All Students")
            print("6. Exit")
            choice = int(input("Enter your choice: "))
            if choice >= 1 and choice <= 5:
                funList[choice]()
            elif choice == 6:
                return
            else:
                print("Invalid choice, please try again.")

manager.main()