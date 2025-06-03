from DBModule_0527 import Database

def output():
    db=Database()
    sql="select * from tb_member"
    rows=db.executeAll(sql)
    for row in rows:
        print(row)
    db.close()

def IdNoDuple(db,user_id):
    sql="""select t.user_id from tb_member t where t.user_id=%s"""
    row=None
    row=db.executeOne(sql,user_id)
    if row!=None : 
        print("Duplicate ID. please Enter different ID.")
        return True
    else : 
        print("You can use this ID!")
        return False
    
def member_register():
    db=Database()
    isDuple=True
    while isDuple:
        user_id=input("Enter ID : ")
        isDuple=IdNoDuple(db,user_id)
    password=input("Enter PASSWORD : ")
    user_name=input("Enter Name : ")
    email=input("Enter email : ")
    phone=input("Enter phoneNumber : ")
    sql="""
        insert into tb_member(user_id, password,user_name,email,phone,regdate)
        values(%s,%s,%s,%s,%s,now());
    """
    db.execute(sql,(user_id,password,user_name,email,phone))
    db.close()
if __name__=="__main__":
    member_register()
    output()
