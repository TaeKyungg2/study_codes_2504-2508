from DBEngine import TheEnginge

class ScoreData:
    def __init__(self):
        self.sname=input("Enter your name : ")
        self.kor=input("Enter kor score : ")
        self.eng=input("Enter eng score : ")
        self.mat=input("Enter mat score : ")
class Manager:
    def main():
        con=TheEnginge()
        while True:
            Manager.printMenu()
            cmd=int(input("Select Number. :"))
            if cmd==1:
                con.GetDataDic()
            elif cmd==2:
                sname=input("Enter to Search name. : ")
                con.SearchData(sname)
            elif cmd==3:
                s=ScoreData()
                con.AddData(s)
            elif cmd==4:
                con=TheEnginge()
            elif cmd==5:
                con.SeeStatic()
            elif cmd==6:
                return
            else:
                print("Wrong Input.")
    def printMenu():
        print("1.See all student")
        print("2.Search student")
        print("3.Add student")
        print("4.New connection")
        print("5.See statistics")
        print("6.Exit")
Manager.main()


