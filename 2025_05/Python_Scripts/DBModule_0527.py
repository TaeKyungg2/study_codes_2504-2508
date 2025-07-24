import pymysql

class Database:
    def __init__(self):
        self.db=pymysql.connect(
            host='localhost', 
            user='user03',
            password='1234',
            db='project1',
            port=3306   #2byte intejer 1~65535
                        #80- http(web server) daum 80
                        #21-telnet 22-ssh 23-ftp
                      )
        self.cursor=self.db.cursor(pymysql.cursors.DictCursor)
    def execute(self,query,args=()):
        print(args)
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
    def close(self):
        if self.db.open:
            self.db.close()