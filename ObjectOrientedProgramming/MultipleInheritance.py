class TeamMember:
    def __init__(self,name,uid):
        self.name = name
        self.uid = uid
class Worker:
    def __init__(self,pay,jobtitle):
        self.pay = pay
        self.jobtitle = jobtitle
class TeamLeader(TeamMember,Worker):
    def __init__(self,name,uid,pay,jobtitle,exp):
        self.exp = exp
        
        Worker.__init__(self,pay,jobtitle)
        TeamMember.__init__(self,name,uid)
        print("Name:{},Pay:{},Exp:{}".format(self.name,self.pay,self.exp))
TL = TeamLeader("Jake",1001,25000,"Scrum Master",5)
print(TeamLeader.mro())
