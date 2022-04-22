import abc
from re import S
from turtle import rt
from xml.etree.ElementPath import prepare_parent 
class member (metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def printPlayerData(self):
        pass
    def calcSalaryPerYear(self):
        pass
    def calcRemainingDuration(self):
        pass    
import datetime
class player (member):
    __pname=None
    __pnumber=None
    __psalary=None
    __signingDate=None
    __contractDuration=None
    __noOfMatches=None

    def __get_pname (self):
        return self.__pname
    def __set_pname (self,s):
        self.__pname=s
        # print("Player's name is updated")
    def __del_pname(self):
        del self.__pname
    pname= property(__get_pname,__set_pname,__del_pname)
    
    def __get_pnumber(self):
        return self.__pnumber
    def __set_pnumber (self,n):
        if 0< n <= 30:
            self.__pnumber=n
            # print("Player's number is updated")
        elif n<0:
            print("number must be positive")
        else:
            print("Player Number shouldn't exceed 30")
    def __del_pnumber(self):
        del self.__pnumber
    pnumber=property(__get_pnumber,__set_pnumber,__del_pnumber)

    def __get_psalary (self):
        return self.__psalary
    def __set_psalary(self,s):
        if 0<s<100000:
            self.__psalary = s
            # print("salary is updated")
        elif s<0:
            print("salary must be positive")
        else:
            print("Player Salary per week shouldn't exceed 100,000")
    def __del_psalary(self):
        del self.__psalary
    psalary = property(__get_psalary,__set_psalary,__del_psalary)

    def __get_contractDuration(self):
        return self.__contractDuration
    def __set_contractDuration(self,y):
        if 0<y<=5:
            self.__contractDuration=y
            # print("Contract duration is updated")
        elif y<0:
            print("Years must be positive")
        else:
            print("Max contract duration is 5 Years")
    def __del_contractDuration(self):
        del self.__contractDuration
    contractDuration=property(__get_contractDuration,__set_contractDuration,__del_contractDuration)

    def __get_signingDate(self):
        return self.__signingDate
    def __del_signingDate(self):
        del self.__signingDate
    signingDate = property(__get_signingDate,__del_signingDate)

    def __get_noOfMatches(self):
        return self.__noOfMatches
    def __set_noOfMatches(self,n):
        self.__noOfMatches=n
        # print("no.of Matches is updated")
    def __del_noOfMatches(self):
        del self.__noOfMatches
    noOfMatches=property(__get_noOfMatches,__set_noOfMatches,__del_noOfMatches)

    def __init__(self,name,number,date,salary=20000,contract=3,matches=0):
        self.pname=name  
        self.pnumber=number
        self.__signingDate=datetime.datetime.strptime(str(date),"%d-%m-%Y").strftime("%d-%m-%Y")
        self.psalary=salary
        self.contractDuration=contract
        self.noOfMatches=matches 

    def printPlayerData(self):
        print("player's data:")
        print("player name is: ",self.pname)
        print("player number is:",self.pnumber)
        print("player salary is: ",self.psalary)
        print("signing date is: ",self.signingDate)
        print("contract duration is: ",self.contractDuration)
        print("number of matches is: ",self.noOfMatches)
    def calcSalaryPerYear(self):
        print("salary per year is:",self.psalary*4*12)
        return self.psalary*4*12
    def calcRemainingDuration(self):
        d1 = datetime.datetime.strptime(self.signingDate,"%d-%m-%Y")
        d2 = datetime.datetime.now()
        r = d2-d1
        z = self.contractDuration*12*30-(r.days)
        if z>0:
            print("The remaining days are: ",format(z,'.1f')," day")
            # print("The remaining weeks are: ",format(z/7,'.1f')," week")
            # print("The remaining years are: ",format(z/(30*12),'.1f'),"Year")
            return z
        else:
            print("error")
            return -1
    def IncreamentMatches(self):
        self.noOfMatches += 1
        print("this match is added")
        return self.noOfMatches
    def increamentContractDutarion(self,y):
        self.contractDuration =+ y
        print("new years are added")
        return self.contractDuration

###################################################

class teamCaptain (player):
    __leadingMatches = None
    __bonus = None
    
    def __get_leadingMatches(self):
        return self.__leadingMatches
    def __del_leadingMatches(self):
        del self.__leadingMatches
    leadingMatches=property(__get_leadingMatches,__del_leadingMatches)

    def __get_bonus(self):
        return self.__bonus
    def __set_bonus(self,b):
        if 0<=b<=100000:
            self.__bonus=b
            # print("bonus is updated")
        elif b<0:
            print("it should be positive")
        else:
            print("Bonus shouldn't exceed 100,000")
    def __del_bonus(self):
        del self.__bonus
    bonus = property(__get_bonus,__set_bonus,__del_bonus)

    def __init__(self, name, number, date, salary=20000, contract=3, matches=0, bonus=5000, leadinMatches=10):
        super().__init__(name, number, date, salary, contract, matches)
        self.bonus=bonus
        self.__leadingMatches=leadinMatches

    def printPlayerData(self):
        super().printPlayerData()
        print("player's bonus is: ",self.bonus)
        print("leading matches are: ",self.leadingMatches)
    def calcSalaryPerYear(self):
        print("salary after bonus is:", self.psalary*4*12 + self.bonus)
        return self.psalary*4*12 + self.bonus
    def increamentLeadingMtaches(self):
         self.leadingMatches +=1
         print("match is added")
         return self.leadingMatches
    def __add__(self, another):
        s = self.psalary + another.psalary
        return s

###################################################

class coach(member):
    __coachName=None
    __coachSalary=None
    __signingDate=None
    __contractDuration=None
    __experienceYears=None
    __bonus=None

    def __get_coachName(self):
        return self.__coachName
    def __set_coachName(self,n):
        self.__coachName=n
    def __del_coachName(self):
        del self.__coachName
    coachName=property(__get_coachName,__set_coachName,__del_coachName)

    def __get_coachSalary(self):
        return self.__coachSalary
    def __set_coachSalary(self, s):
        if 0<= s <= 200000:
            self.__coachSalary=s
            # print("salary is updated")
        elif s<0:
             print("salary must be positive")
        else:
            print("Coach Salary per week shouldn't exceed 100,000")
    def __del_coachSalary(self):
        del self.__coachSalary
    coachSalary=property(__get_coachSalary,__set_coachSalary,__del_coachSalary)

    def __get_contractDuration(self):
        return self.__contractDuration
    def __set_contractDuration(self,y):
        if 0<y<=3:
            self.__contractDuration=y
            # print("Contract duration is updated")
        elif y<0:
            print("Years must be positive")
        else:
            print("Max contract duration is 3 Years")
    def __del_contractDuration(self):
        del self.__contractDuration
    contractDuration=property(__get_contractDuration,__set_contractDuration,__del_contractDuration)

    def __get_signingDate(self):
        return self.__signingDate
    def __del_signingDate(self):
        del self.__signingDate
    signingDate = property(__get_signingDate,__del_signingDate)

    def __get_experienceYears(self):
        return self.__experienceYears
    def __set_experienceYears(self,y):
        if y>=8:
            self.__experienceYears = y
        elif y<0:
            print("Years must be positive")
        else:
            print("Experience Years should be greater than or equal 8 years")
    def __del_experienceYears(self):
        del self.__experienceYears
    experienceYears=property(__get_experienceYears,__del_experienceYears)

    def __get_bonus(self):
        return self.__bonus
    def __set_bonus(self,b):
        if 0<=b<=50000:
            self.__bonus=b
            # print("bonus is updated")
        elif b<0:
            print("it should be positive")
        else:
            print("Bonus shouldn't exceed 50,000")
    def __del_bonus(self):
        del self.__bonus
    bonus = property(__get_bonus,__set_bonus,__del_bonus)

    def __init__(self,name,experienceYears,signingDate,salary=50000,contract=2,bonus=10000):
        self.coachName=name
        self.__set_experienceYears(experienceYears)
        self.__signingDate=datetime.datetime.strptime(str(signingDate),"%d-%m-%Y").strftime("%d-%m-%Y")
        self.coachSalary=salary
        self.contractDuration=contract
        self.bonus=bonus

    def printPlayerData(self):
        print("Coach's data:")
        print("Coach name is: ",self.coachName)
        print("Coach salary is: ",self.coachSalary)
        print("signing date is: ",self.signingDate)
        print("contract duration is: ",self.contractDuration)
        print("Experience Years are: ",self.experienceYears)
        print("bonus is: ",self.bonus)
    def calcSalaryPerYear(self):
        return self.coachSalary*4*12
    def calcRemainingDuration(self):
        d1 = datetime.datetime.strptime(self.signingDate,"%d-%m-%Y")
        d2 = datetime.datetime.now()
        r = d2-d1
        z = self.contractDuration*12*30-(r.days)
        if z>0:
            print("The remaining days are: ",format(z,'.1f')," day")
            # print("The remaining weeks are: ",format(z/7,'.1f')," week")
            # print("The remaining years are: ",format(z/(30*12),'.1f'),"Year")
            return z
        else:
            print("error")
            return -1
    
    def increamentExperienceYears(self):
        self.__experienceYears +=1
        return self.__experienceYears
    def addBonus(self,b):
        try:
            self.bonus = b
        except:
            print('bonus is too much:')

###################################################

class team:
    __teamName=None
    __teamPosition=None
    __coach=None
    __playersList=None
    __teamCaptain=None
    __numberOfPlayers=None

    def __get_teamName(self):
        return self.__teamName
    def __set_teamName(self,n):
        self.__teamName=n
        # print("team name is updated")
    def __del_teamName(self):
        del self.__teamName
    teamName=property(__get_teamName,__set_teamName,__del_teamName)

    def __get_teamPosition(self):
        return self.__teamPosition
    def __set_teamPosition(self,n):
        self.__teamPosition=n
        # print("team position is updated")
    def __del_teamPosition(self):
        del self.__teamPosition
    teamPosition=property(__get_teamPosition,__set_teamPosition,__del_teamPosition)

    def __get_coach(self):
        return self.__coach
    def __set_coach(self,c):
        self.__coach=c
        # print("coach is updated")
    def __del_coach(self):
        del self.__coach
    coach=property(__get_coach,__set_coach,__del_coach)

    def __get_playersList(self):
        return self.__playersList
    def __set_playersList(self,l):
        self.__playersList=l
        # print("players list is updated")
    def __del_playersList(self):
        del self.__playersList
    playersList=property(__get_playersList,__set_playersList,__del_playersList)

    def __get_teamCaptain(self):
        return self.__teamCaptain
    def __set_teamCaptain(self,n):
        self.__teamCaptain=n
        # print("team captain is updated")
    def __del_teamCaptain(self):
        del self.__teamCaptain
    teamCaptain=property(__get_teamCaptain,__set_teamCaptain,__del_teamCaptain)

    def __get_numberOfPlayers(self):
        return self.__numberOfPlayers
    def __del_numberOfPlayers(self):
        del self.__numberOfPlayers
    numberOfPlayers=property(__get_numberOfPlayers,__del_numberOfPlayers)

    def __init__(self,teamName,teamPosition,coach,noOfPlayers=0,playerList=[],teamCaptain=None):
        self.teamName=teamName
        self.teamPosition=teamPosition
        self.coach=coach
        self.__numberOfPlayers=noOfPlayers
        self.playersList=playerList
        self.teamCaptain=teamCaptain

    def printTeamData(self):
        print("Team Data: ")
        print("Team name is: ",self.teamName)
        print("Team position is: ",self.teamPosition)
        print("Team coach is: ",self.coach.coachName)
        print("Number of players is: ",self.numberOfPlayers)
        for i in self.playersList:
            print("Team players are: ",i.pname)
        if self.teamCaptain:            
            print("Team captain is: ",self.teamCaptain.pname)

    def printCaptainInfo(self):
        print("Captain's data:")
        print("Captain name is: ",self.teamCaptain.pname)
        print("Captain number is:",self.teamCaptain.pnumber)
        print("Captain salary is: ",self.teamCaptain.psalary)
        print("signing date is: ",self.teamCaptain.signingDate)
        print("contract duration is: ",self.teamCaptain.contractDuration)
        print("number of matches is: ",self.teamCaptain.noOfMatches)
        print("Captain's bonus is: ",self.teamCaptain.bonus)
        print("leading matches are: ",self.teamCaptain.leadingMatches)

    def addPlayer(self,pname,pnumber,psalary,signingDate,contract,noOfMatches):
        try:
            exist = False
            for i in self.playersList:
                if i.pnumber == pnumber:
                    
                    exist = True
                    break               
            if exist :
                print("This player is already exist!")
            else:
                p=player(pname,pnumber,signingDate,psalary,contract,noOfMatches)
                self.playersList.append(p)
                self.__numberOfPlayers +=1
                self.modifyTheCaptain()  
                print("player is added") 
        except:
             print("can't add this player!")       
    
    def calcAllSalary(self):
        s = 0
        for i in self.playersList:
            s += i.psalary
        r = s + self.coach.coachSalary
        return r

    def searchPlayer(self,pnumber):
        found = False
        for i in self.playersList:
            if i.pnumber == pnumber:
                found = True
                i.printPlayerData()
                break   
        if not found:
            print("this number is empty!")

    def deletePlayer(self,pnumber):
        found = False
        for i in self.playersList:
            if i.pnumber == pnumber:
                found=True
                self.playersList.remove(i)
                self.__numberOfPlayers -=1
                print("player removed")
                break   
            
        if found == False:
            print("this number is empty!")
        self.modifyTheCaptain()

   
    
    def modifyTheCaptain(self,bonus=5000,NumberOfMatches=10):
        maxNo=0
        newTeamCaptain=0
        for i in self.playersList:
            if i.noOfMatches > maxNo:
               maxNo = i.noOfMatches
               newTeamCaptain=i
        captain=teamCaptain(newTeamCaptain.pname,newTeamCaptain.pnumber,newTeamCaptain.signingDate,newTeamCaptain.psalary,newTeamCaptain.contractDuration,newTeamCaptain.noOfMatches,bonus=bonus,leadinMatches=NumberOfMatches)
        self.teamCaptain=captain  


    def __len__(self):
        return len(self.playersList)
        
    def __getitem__(self,pnumber):
        found = False
        for i in self.playersList:
            if i.pnumber == pnumber:
                found = True
                i.printPlayerData()
                break   
        if not found:
            print("this number is empty!")    
               
###################################################


c = coach("coatch1",10,'02-06-2020')
t = team("team1",2,c)
t.addPlayer("player1",1,50000,'22-05-2020',3,1)
t.addPlayer("player2",7,10000,'21-05-2020',3,2)
t.addPlayer("player3",9,30000,'13-07-2021',3,1)
t.addPlayer("player4",3,25000,'08-02-2020',3,3)
print("------------")
print("length of team is",len(t))
print("------------")
t.printCaptainInfo()
print("------------")
t.printTeamData()
print("------------")
print(t.calcAllSalary())
print("------------")
t.searchPlayer(10)
print("------------")
t[10]
print("------------")
t.deletePlayer(6)
print("------------")
t.printCaptainInfo()
print("------------")
t.printTeamData()
print("------------")
print("length of team is",len(t))
print("------------")
print(t.calcAllSalary())

