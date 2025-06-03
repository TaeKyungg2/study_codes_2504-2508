import pymysql

class Database:

    @staticmethod
    def Connection(func):
        Data=Database.__new__(Database)
        def inner(cls,*arg,**kwarg):
            Data.db=pymysql.connect(
            host='localhost', 
            user='user03',
            password='1234',
            db='project1',
            port=3306)
            Data.cursor=Data.db.cursor(pymysql.cursors.DictCursor)
            func(cls,Data,*arg,**kwarg)
            Data.db.commit()
            Data.db.close()
            return
        return inner

    def execute(self,query,args=()):
        self.cursor.execute(query,args)
        self.db.commit()

    def executeOne(self,query,args=()):
        self.cursor.execute(query,args)
        row=self.cursor.fetchone()
        return row
    
    def executeAll(self,query,args=()):
        self.cursor.execute(query,args)
        rows=self.cursor.fetchall()
        return rows
