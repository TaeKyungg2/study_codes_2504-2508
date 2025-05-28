from sqlalchemy import text,create_engine
class TheEnginge():
    theEngine = create_engine("mysql+pymysql://root:1234@localhost:3306/sakila",
                       pool_size=10,
                       max_overflow=5,
                       pool_recycle=3600
                       , echo=True, future=True)
    
    def __init__(self):
        print("New Connection")
        self.con=self.theEngine.connect()

    def GetDataDic(self):
        result=self.con.execute(text(
            """select concat(c.first_name,' ',c.last_name) as name, a.address,a.district,a.postal_code
from customer c
join address a on a.address_id=c.address_id"""))
        dics=result.mappings().all()
        for row in dics:
            print(row)
        return
    def SearchData(self,name):
        result=self.con.execute(text("""select * from(select concat(c.first_name,' ',c.last_name) as name, a.address,a.district,a.postal_code
from customer c
join address a on a.address_id=c.address_id) as x where x.name=:name"""),{"name":name})
        dic=result.mappings().all()
        for row in dic:
            print(row)
        return
    def SeeStatic(self):
        result=self.con.execute(text("""select '모든 사람', count(*)
from (select concat(c.first_name,' ',c.last_name) as name, a.address,a.district as di,a.postal_code
from customer c
join address a on a.address_id=c.address_id)as x
union
select count(*),x.di
from (select concat(c.first_name,' ',c.last_name) as name, a.address,a.district as di,a.postal_code
from customer c
join address a on a.address_id=c.address_id)as x
group by x.di"""))
       
        for row in result:
            print(row)
        return
        
        
        

