from aDBEngine import TheEnginge

class Customer:
    def __init__(self):
        self.name=input("Enter your name : ")
        self.postal_code=input("Enter postal code: ")
        self.address=input("Enter your address : ")
class Manager:
    def main():
        con=TheEnginge()
        while True:
            Manager.printMenu()
            cmd=int(input("Select Number. :"))
            if cmd==1:
                con.GetDataDic()
            elif cmd==2:
                name=input("Enter to Search name. : ")
                con.SearchData(name)
            elif cmd==4:
                con=TheEnginge()
            elif cmd==5:
                con.SeeStatic()
            elif cmd==6:
                return
            else:
                print("Wrong Input.")
    def printMenu():
        print("1.See all customer")
        print("2.Search customer")
        print("4.New connection")
        print("5.See district statistics")
        print("6.Exit")
Manager.main()


