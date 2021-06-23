import pymysql

myconn = pymysql.connect(host="localhost", user="root", passwd="", database="event_management")
cur = myconn.cursor()
#cur.execute("insert into tblperson values('Rey','Sighaniya')")
cur.execute("select * from admin where admin_name='Harshil'" )
result = cur.fetchall()
print(result)
for x in result:
   print(x)
myconn.close()
