import time
import csv
import os 
import sqlite3







#       ,-=-.       ______     _
#      /  +  \     />----->  _| |_
#      | ~~~ |    // -/- /  |_   _|
#      |R.I.P|   //  /  /     | |
# \vV,,|_____|V,//_____/VvV,v,|_|/,,vhjwv/,#
#
#
#       ,-=-.       ______     _
#      /  +  \     />----->  _| |_
#      | ~~~ |    // -/- /  |_   _|
#      |R.I.P|   //  /  /     | |
# \vV,,|_____|V,//_____/VvV,v,|_|/,,vhjwv/,#
#       ,-=-.       ______     _
#      /  +  \     />----->  _| |_
#      | ~~~ |    // -/- /  |_   _|
#      |R.I.P|   //  /  /     | |
# \vV,,|_____|V,//_____/VvV,v,|_|/,,vhjwv/,#
#       ,-=-.       ______     _
#      /  +  \     />----->  _| |_
#      | ~~~ |    // -/- /  |_   _|
#      |R.I.P|   //  /  /     | |
# \vV,,|_____|V,//_____/VvV,v,|_|/,,vhjwv/,#
#       ,-=-.       ______     _
#      /  +  \     />----->  _| |_
#      | ~~~ |    // -/- /  |_   _|
#      |R.I.P|   //  /  /     | |
# \vV,,|_____|V,//_____/VvV,v,|_|/,,vhjwv/,#
#       ,-=-.       ______     _
#      /  +  \     />----->  _| |_
#      | ~~~ |    // -/- /  |_   _|
#      |R.I.P|   //  /  /     | |
# \vV,,|_____|V,//_____/VvV,v,|_|/,,vhjwv/,#
#
#
#
#
#
#
#
#
















def anigilate(date1,date2):
        
        y2 = time.strptime(date2,"%H.%M.%d.%m.%Y")
        
        return time.mktime(y2)-date1   
class Todolist:
    def __init__(self,filename):
        self.filename = filename
       
        self.respect = 0 
        self.connect = sqlite3.connect(f"{self.filename}.db")

        self.cursr = self.connect.cursor()
        self.cursr.execute("""CREATE TABLE IF NOT EXISTS users 
                    (id INTEGER PRIMARY KEY,
                    name TEXT
                    
                    )
                    
                    """)

        self.cursr.execute("""CREATE TABLE IF NOT EXISTS tasks 
                    (id INTEGER PRIMARY KEY,
                        userid INTEGER,
                        name TEXT,
                        text TEXT,
                        time INT,
                        status BOOL,
                        FOREIGN KEY (userid) REFERENCES users (id)
                    )""")
        # Эта строчка кода заменяется на cursore.execute
        
        self.connect.commit()
    def create(self,name,text,time):
        # Эта строчка заменяется на insert 
        self.cursr.execute(f"""INSERT INTO tasks (id,userid,name,text,time,Status) VALUES(1,11,'выжить','Алкоголизм',1231241232,false)  """)
        #self.cursr.fetchall
        self.sync()

    def Read(self):
        # эта строчка заменяется на select 
        self.cursr.execute("""SELECT * FROM tasks
                    """)
        return self.cursr.fetchall()

    def update_task(self,num_of_change,status):
        # ВОТ ЭТО Я ХЕЗЕ КАК ЗАМЕНИТЬ 
        try:
            

                    
            num_of_change = int(num_of_change)
            self.cursr.execute(f"""UPDATE tasks SET status={status} WHERE id = {num_of_change}
                    """)
                    
                    
                    
            # if status.lower() == "true" or status.lower() == "1":
                    
                    
            #     print(anigilate(time.time(),self.NST_arr[num_of_change][2]))
            #     if anigilate(time.time(),self.NST_arr[num_of_change][2]) >0 :

            #         self.respect+=1
            #     else:
            #         self.respect-=1
                    
                
                    
                
            # else:
            #     print("ERORRRRRR REMAAAAKEEEE")
        except:
            print("поаккуратней")

        self.sync()

    def delete(self,num_of_change):
        
        try:
            

                    
            num_of_change = int(num_of_change)
            self.cursr.execute(f"""DELETE FROM tasks WHERE id={num_of_change}
                    """)
                    
                    
                    
                # if status.lower() == "true":
                    
                #     self.NST_arr[num_of_change][3] = True
                #     print(anigilate(time.time(),self.NST_arr[num_of_change][2]))
                #     if anigilate(time.time(),self.NST_arr[num_of_change][2]) >0 :

                #         self.respect+=1
                #     else:
                #         self.respect-=1
                    
                # else:
                #     print("TASK NOT MADE")
                    
                
            # else:
            #     print("ERORRRRRR REMAAAAKEEEE")
        except:
            print("поаккуратней")

        self.sync()
        
        self.sync()
    def sync(self):
        self.connect.commit()
    
