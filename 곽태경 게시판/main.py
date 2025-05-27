import pickle
from datetime import datetime
from time import sleep
import re
import random
from clear import classClear

@classClear
class Member:
    memberList=[]
    noDup=set()
    def __init__(self,id):
        self.number=self.makeNumber()
        self.id=id
        self.password=input('사용할 비밀번호를 입력하세요 :')
        self.name=input('이름을 입력하세요 :')
        self.phone=self.checkPhone()
        self.mail=self.checkEmail()
        self.addMember()
    def makeNumber(self):
        while True:
            number=random.randint(100,999)
            if number not in Member.noDup:
                Member.noDup.add(number)
                return number
    def checkPhone(self):
        while True:
            number=input('휴대폰 번호를 입력하세요(-포함) :')
            if re.match(r'\d{3}-\d{3,4}-\d{4}',number):
                return number
            else:
                print('형식에 맞지 않습니다.')
    def checkEmail(self):
        while True:
            email=input('이메일을 입력하세요 >')
            if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,4}$',email):
                return email
            else:
                print('형식에 맞지 않습니다.')
    def dataModify(self):
        sel={1:'id',2:'password',3:'name',4:'phone',5:'mail'}
        for i in sel:
            print(f'{i}.{sel[i]}',end=' ')
        print()
        print('어떤 정보를 수정하시겠습니까?',end='')
        cmd=int(input('번호 >'))
        if cmd ==4:
            self.phone=self.checkPhone()
        elif cmd==5:
            self.mail=self.checkEmail()
        elif cmd==1 or cmd==2 or cmd==3:
            setattr(self,sel[cmd],input(f'새로운 {sel[cmd]}를 입력하세요.'))
        else:
            print('잘못된 입력입니다.')
            return
        print(f'{sel[cmd]}가 {getattr(self,sel[cmd])}로 수정되었습니다.')
        self.save()
    def humanPrint(self):
        print(f'번호 : {self.number} {self.name} ID : {self.id} 전화번호 : {self.phone}, 이메일 : {self.mail}')
        cmd=input('뒤로가시려면 0을 입력하세요 >')
        if cmd=='0': return
        else:
            print('잘못된 입력입니다.')
            sleep(1)

    @staticmethod
    def devMakeMember(num):
        member=Member.__new__(Member)
        member.number=num
        member.noDup.add(num)
        member.id=f'id{num}'
        member.password=f'pw{num}'
        member.name=f'테스트{num}'
        member.phone=f'010-'+f'{num}'*4+'-'+f'{num}'*4
        member.mail=f'{num}'*4+'@'+f'{num}'*4+'.com'
        member.noDup.add(member.number)
        member.addMember()
        return member
    def addMember(self):
        self.memberList.append(self)
        self.save()
    def removeMember(self):
        self.memberList.remove(self)
        self.noDup.remove(self.number)
        self.save()
    def save(self):
        with open('MemberDATA.p', 'wb') as f:
                pickle.dump(self.memberList, f)

@classClear
class Post:
    postList=[]
    def __init__(self,human):
        self.writerName=human.name
        self.memberNumber=human.number
        self.title=input('제목을 입력하세요 :')
        self.story=input('내용을 입력하세요 :')
        self.date=datetime.now()
        self.viewCount=0
        self.addPost()
    def addPost(self):
        self.postList.append(self)
    def removePost(self):
        self.postList.remove(self)

    @classmethod
    def BoardMain(cls):
        while True:
            cls.printAll()
            print('1.글 보기 2.글쓰기 3.나가기')
            cmd=input('숫자를 입력하세요 >')
            if cmd=='1':
                if len(cls.postList)==0:
                    print('글이 없습니다.')
                    sleep(1)
                else :
                    num=int(input("볼 글번호를 입력하세요 >"))
                    if len(cls.postList)>=num : 
                        cls.postList[num-1].postMain()
                    else:
                        print('잘못된 입력입니다.')
                        sleep(1)
            elif cmd=='2':
                if TaeKyung.nowLoginMan==None:
                    print('접근 권한이 없습니다.')
                    sleep(1)
                else: cls(TaeKyung.nowLoginMan)
            elif cmd=='3' :
                print('게시판을 나갑니다.')
                sleep(1)
                return
                
    def printAll():
        print('<게시판>')
        for i,post in enumerate(Post.postList):
            print(f'{i+1}) 제목 : {post.title} 작성자 : {post.writerName} {post.memberNumber} 조회수 : {post.viewCount}')
    
    def postMain(self):
        self.see()
        while True:
            print('1.나가기 2.수정하기 3.삭제하기')
            cmd=input('번호 >')
            if cmd=='1':
                return
            elif cmd=='2':
                self.postModify()
            elif cmd=='3':
                if not self.humanCheck():
                    return
                self.removePost()
                print('삭제되었습니다.')
                sleep(1)
                return
            
    def humanCheck(self):
        if TaeKyung.nowLoginMan==None or self.writerName!=TaeKyung.nowLoginMan.name:
            print('이 글에 대한 권한이 없습니다.')
            sleep(1)
            return False
        return True

    def postModify(self):
        if not self.humanCheck() :
            return
        print('1.제목 2.내용')
        print('어떤 정보를 수정하시겠습니까? 숫자입력',end='')
        cmd=int(input('>'))
        if cmd==1:
            self.title=input('새로운 제목을 입력하세요 >')
        elif cmd==2:
            self.story=input('새로운 내용을 입력하세요 >')
        else:
            print('잘못된 입력입니다.')
            return
        print('수정되었습니다.')
        self.see()
        self.save()

    def see(self):
        print(f'<{self.title}> by{self.writerName}')
        print(f'작성시간 : {self.date} 조회수 : {self.viewCount}\n'+'-'*20)
        print(self.story)
        self.viewCount+=1
        self.save()

    def save(self):
        with open('PostDATA.p', 'wb') as f:
                pickle.dump(self.postList, f)

    @staticmethod
    def devMakePost(writer):
        post=Post.__new__(Post)
        post.writerName=writer.name 
        post.memberNumber=writer.number
        post.title=f'제목{writer.number}'
        post.story=f'내용{writer.number}'*100
        post.date=datetime.now()
        post.viewCount=0
        post.addPost()
        return post

@classClear
class Manager:
    def __init__(self):
        self.nowLoginMan=None
        self.welcome()
    
    def getData(self):
        try:
            with open('MemberDATA.p', 'rb') as f:
                Member.memberList=pickle.load(f)
        except:
            with open('MemberDATA.p', 'wb') as f:
                pickle.dump(Member.memberList, f)
        try:
            with open('PostDATA.p', 'rb') as f:
                Post.postList=pickle.load(f)
        except:
            with open('PostDATA.p', 'wb') as f:
                pickle.dump(Post.postList, f)
    def welcome(self):
        for i in 'Welcome to TaeKyung\'s board':
            print(i,end='',flush=True)
            sleep(0.02)
        print()
        sleep(1)
        
    def main(self):
        Member.memberList=[]
        self.getData()
        while True:
            TaeKyung.printMenu()
            cmd=input("번호를 선택하세요. > ")
            if cmd=='1':
                self.join()
            elif cmd=='2':
                self.login()
            elif cmd=='3':
                Post.BoardMain()
            elif cmd=='4':
                print('종료합니다.')
                break
            elif re.match(r'[7]{5,20}',cmd):
                dev=Developer()
                dev.DeveloperMain()
        
    def printMenu(self):
        print('1.회원가입 2.로그인 3.게시판 가기 4.종료')

    def login(self):
        while True:
            id=input('아이디를 입력하세요. \n 뒤로 가시려면 0을 입력하세요.\n>')
            if id==0 : return
            human=list(filter(lambda x : False if x==None else x.id==id,Member.memberList))
            if human==[] : 
                print('아이디 정보가 없습니다.')
                sleep(1)
                return
            human=human[0]
            pw=input('패스워드를 입력하세요 > ')
            if human.password==pw:
                self.nowLoginMan=human
                print(f'{human.name}으로 로그인 되었습니다.')
                sleep(1)
                self.loginMain(human)
                return
            else : 
                print('비밀번호가 잘못되었습니다.')
                sleep(1)

    def printLogMenu(self):
         print('1.회원정보 수정 2.회원 탈퇴 3.회원정보 조회 4.게시판 가기 5.뒤로가기 6.로그아웃')

    def loginMain(self,human):
        while True:
            self.printLogMenu()
            cmd=input('>')
            if cmd=='1':
                human.dataModify()
            elif cmd=='2':
                Member.removeMember(human)
                print('탈퇴되었습니다.')
                sleep(1)
                return
            elif cmd=='3':
                human.humanPrint()
            elif cmd=='4':
                Post.BoardMain()
            elif cmd=='5':
                print('나가겠습니다.')
                return
            elif cmd=='6':
                self.nowLoginMan=None
                print('로그아웃 되었습니다.')
                sleep(1)
                return
            else : 
                print('잘못된 입력입니다.')
                sleep(1)

    def join(self):
        while True:
            id=input('사용할 아이디를 입력하세요 >')
            if list(filter(lambda x : False if x==None else x.id==id,Member.memberList))!=[]:
                print('중복되는 아이디가 있습니다. 다른 아이디를 입력해주세요.')
            else : break
        new=Member(id)

@classClear
class Developer:
    __instance=None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        self.name='Developer'
        self.id='dev'

    def testCase(self):
        if len(Member.memberList)>0:
            Member.memberList=[]
        if len(Post.postList)>0:
            Post.postList=[]
        for num in range(1,8):
            member=Member.devMakeMember(num)
            Post.devMakePost(member)
        print('테스트 케이스가 생성되었습니다.')
        sleep(1)

    def welcome(self):
        for i in range(20):
            print('#',end='',flush=True)
            sleep(0.02)
        print()
        for i in 'Welcome Developer Mode':
            print(i,end='',flush=True)
            sleep(0.04)
        print()
        for i in range(20):
            print('#',end='',flush=True)
            sleep(0.02)
        print()
        sleep(2)
    def DeveloperMain(self):
        self.welcome()
        while True:
            print('1.회원 데이터 관리 2.게시판 데이터 관리 3.테스트케이스 생성(전체 초기화) 4.나가기')
            cmd=input('>')
            if cmd=='1':
                self.memData()
            elif cmd=='2':
                self.postData()
            elif cmd=='3':
                self.testCase()
            elif cmd=='4':
                print('나가겠습니다.')
                sleep(1)
                return
            else:
                print('잘못된 입력입니다.')
    def memData(self):
        if Member.memberList:
            for member in Member.memberList:
                print(f'({member.number})아이디 : {member.id} 비밀번호 : {member.password} 이름 : {member.name} 전화번호 : {member.phone} 이메일 : {member.mail}')
            cmd=int(input('나가기는 0, 강퇴는 회원번호를 입력하세요 >'))
            if cmd==0: return
            elif cmd in Member.noDup:
                member=next(filter(lambda x : x.number==cmd,Member.memberList))
                Member.removeMember(member)
                print('강퇴되었습니다.')
            else :
                print('잘못된 입력입니다.')
                sleep(1)
    def postData(self):
        if Post.postList:
            for i,post in enumerate(Post.postList):
                print(f'({i})제목 : {post.title} 작성자 : {post.writerName} {post.memberNumber} 조회수 : {post.viewCount}')
            cmd=int(input('나가기는 0, 삭제는 글번호를 입력하세요 >'))
            if cmd==0: return
            elif 0<cmd and cmd<len(Post.postList):
                del Post.postList[cmd]
                print('삭제되었습니다.')
        else:
            print('게시글이 없습니다.')
            sleep(1)
TaeKyung=Manager()
TaeKyung.main()
