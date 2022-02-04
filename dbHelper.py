import mysql.connector as connector
tablename = "harman"
class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost', 
                                     port='3306',
                                     user = 'root', 
                                     password='admin', 
                                     database='pythondb' )
    def create_table(self):
        query = f'create table if not exists {tablename}(userId int primary key,userName varchar(200), phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print('Table created')

    def insertDataToTable(self,userId,userName,phone):
        query = f"insert into {tablename}(userId,userName,phone) values({userId},'{userName}', '{phone}')"
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('Value inserted')

    def fetchAlldata(self):
        query = f"select * from {tablename};"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)


    def fetchUser(self,userId):
        query = f"select * from {tablename} where userId={userId};"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)
    
    def deleteUser(self, userId):
        query = f"delete from {tablename} where userId = {userId}"
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

    def updateUser(self, userId, newName, newPhone):
        query = f"update {tablename} set userName='{newName}',phone='{newPhone}' where userId={userId}"
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")