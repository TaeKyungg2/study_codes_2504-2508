from sqlalchemy import text,create_engine
class TheEnginge():
    theEngine = create_engine("mysql+pymysql://root:1234@localhost:3306/mydb2",
                       pool_size=10,
                       max_overflow=5,
                       pool_recycle=3600
                       , echo=True, future=True)
    trigger=text("""create trigger dat
    before insert on tb_score
	FOR EACH ROW
    begin
	set new.grade = case when new.average between 90 and 100 then "A"
						when new.average between 80 and 89 then "B"
						when new.average between 70 and 79 then "C"
						when new.average between 60 and 69 then "D"
						else "E"
				end;
            end
""")
    def __init__(self):
        print("New Connection")
        self.con=self.theEngine.connect()
        #self.con.execute(TheEnginge.trigger)
    def GetDataDic(self):
        result=self.con.execute(text("select * from tb_score"))
        dics=result.mappings().all()
        for row in dics:
            print(row)
        return
    def SearchData(self,sname):
        result=self.con.execute(text("select * from tb_score t where t.sname=:sname"),{"sname":sname})
        dic=result.mappings().all()
        for row in dic:
            print(row)
        return
    def AddData(self,data):
        self.con.execute(text("""INSERT INTO tb_score (sname, kor,mat,eng) 
                              VALUES (:s,:k,:m,:e)"""),{"s":data.sname,"k":data.kor,"m":data.mat,"e":data.eng})
        self.con.commit()
    def SeeStatic(self):
        result=self.con.execute(text("""select count(*),t.grade
from tb_score t 
group by t.grade"""))
        result=self.con.execute(text("select count(*) as stuCount from tb_score"))
        for row in result:
            print(row)
        result=self.con.execute(text("select count(*) c,t.grade from tb_score t group by t.grade"))
        for row in result:
            print(row)
        return
        
        
        

