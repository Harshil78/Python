from datetime import datetime,date
from datetime import timedelta

class mydate():
    def __init__(self):
        self.day=int(input("Enter Day:-"))
        self.month = int(input("Enter Month:-"))
        self.year = int(input("Enter Year:-"))

    def addDays(self,mydate,value):
        getdate=date(self.year,self.month,self.day)
        if value>0:
            newdate=getdate+timedelta(days=value)

        elif value<0:
            v=abs(value)
            newdate=getdate-timedelta(days=v)

        else:
            print("Insert Date Properly")
        return newdate

    def formatdate(self,mydate,formatstring):
        newdate=mydate.addDays(mydate,value)
        print("Date After Increasing or Decreasing Days:-",newdate)
        if formatstring=="dd-mm-yyyy":
            print("New Date According To New Format(dd-mm-yyyy) :-",newdate.strftime('%d-%m-%Y'))
        elif formatstring=="mm-dd-yyyy":
            print("New Date According To New Format(mm-dd-yyyy) :-",newdate.strftime('%m-%d-%Y'))
        elif formatstring=="yyyy-mm-dd":
            print("New Date According To New Format(dd-mm-yyyy) :-",newdate)
        else:
            print("Invalid Date Format")
mydate=mydate()
value=int(input("Enter Value To increase or decrease Date:- "))
formatstring=input("Enter date format either dd-mm-yyyy,mm-dd-yyyy or yyyy-mm-dd :- ")
mydate.addDays(mydate,value)
mydate.formatdate(mydate,formatstring)