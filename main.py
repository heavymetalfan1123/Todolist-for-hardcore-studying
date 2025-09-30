
import os
import time
import sqlite3


# def anigilate(date1,date2):
        
#         y2 = time.strptime(date2,"%H.%M.%d.%m.%Y")
        
#         return time.mktime(y2)-date1   
# позже будет добавленна логика по времени 
class Todolist: 
    def __init__(self,filename):

        self.filename = filename
        self.respect = 0 
        self.connect = sqlite3.connect(f"{self.filename}.db")
        self.cursr = self.connect.cursor()
        self.cursr.execute("""CREATE TABLE IF NOT EXISTS users 
                    (id INTEGER PRIMARY KEY,
                    name TEXT,
                    pas TEXT
                    ) """)

        self.cursr.execute("""CREATE TABLE IF NOT EXISTS tasks 
                    (id INTEGER PRIMARY KEY,
                        userid INTEGER,
                        name TEXT,
                        text TEXT,
                        time TEXT,
                        status BOOL,
                        FOREIGN KEY (userid) REFERENCES users (id)
                    )""")
       
        
        self.connect.commit()
    def create(self,name,text,time,userid):
        
        self.cursr.execute("""SELECT * FROM tasks""")
        result = self.cursr.fetchall()
        print(len(result))
        self.cursr.execute(f"""INSERT INTO tasks (id,userid,name,text,time,Status) VALUES({len(result)+1},'{userid}','{name}','{text}','{time}',false)  """)
        #self.cursr.fetchall
        self.sync()

    def Read(self,id):
        
        self.cursr.execute(f"""SELECT * FROM tasks WHERE userid = {id}
                    """)
        return self.cursr.fetchall()

    def update_task(self,num_of_change,status,usrid):
        
        try:
            num_of_change = int(num_of_change)
            self.cursr.execute(f"""UPDATE tasks SET status={status} WHERE id = {num_of_change} AND userid = {usrid}
                    """)
                    
                    
                    
            
           
        except:
            print("поаккуратней")

        self.sync()

    def delete(self,num_of_change,usrid):
        
        try:
            
            num_of_change = int(num_of_change)
            self.cursr.execute(f"""DELETE FROM tasks WHERE id={num_of_change} AND userid = {usrid}
                    """)
                    
                    
                    
                
        except:
            print("поаккуратней")

        self.sync()
        
        
    def sync(self):
        self.connect.commit()
    
class User:
    
    def __init__(self,filename):

        self.filename = filename
        self.currentuser = 0 
        self.connect = sqlite3.connect(f"{self.filename}.db")

        self.cursr = self.connect.cursor()
        
        
        self.cursr.execute(f"""SELECT * FROM users """)
        res = self.cursr.fetchall()
        
        if len(res) <= 0  and len(name)>0:
            print("""╔══════════════════════════════════════════════╗
║            ДОБРО ПОЖАЛОВАТЬ!                 ║
╠══════════════════════════════════════════════╣
║ Обнаружена пустая база данных                ║
║ Сейчас будет создан первый аккаунт           ║
║                                              ║
║ Это займет менее минуты...                   ║
╚══════════════════════════════════════════════╝""")
            self.create(input("Введите имя: "),input("Введите пароль: "))
        

    def validate(self,name,pas):

        self.cursr.execute(f"""SELECT * FROM users WHERE name = '{name}' AND pas = '{pas}'""")
        res = self.cursr.fetchall()
       
        if len(res):
            self.currentuser = res[0][0]
            return True 
        else: return False 

    def create(self,name,text):
        

        self.cursr.execute("""SELECT * FROM users""")
        result = self.cursr.fetchall()
        #print(len(result))
        self.cursr.execute(f"""SELECT * from users WHERE name = '{name}'""")
        res1 =  self.cursr.fetchall()
        #print(res1,result)
        if len(res1) <=0:
            self.cursr.execute(f"""INSERT INTO users (id,name,pas) VALUES({len(result)+1},'{name}','{text}')  """)
            self.currentuser = len(result)+1
            #self.cursr.fetchall
            self.sync()
            print("""╔══════════════════════════════════════════════╗
    ║            АККАУНТ СОЗДАН!                   ║
    ╠══════════════════════════════════════════════╣
    ║ Первый пользователь добавлен в систему       ║
    ║ Теперь вы можете войти под своими данными    ║
    ╚══════════════════════════════════════════════╝""")
        

    def sync(self):
        self.connect.commit()




dec = Todolist("List")

usr = User("List")



print("""╔══════════════════════════════════════════════╗
║            ДОБРО ПОЖАЛОВАТЬ!                 ║
╠══════════════════════════════════════════════╣
║ База данных обнаружена                       ║
║ Вы можете войти в существующий аккаунт       ║
║ или создать новый                            ║
╚══════════════════════════════════════════════╝""")


regis = True

while regis:
    mode = input("""╔══════════════════════════════════════════════╗
║            РЕГИСТРАЦИЯ И ВХОД                ║
╠══════════════════════════════════════════════╣
║ [1] 📝 Создать новый аккаунт                 ║
║ [2] 🔐 Войти в существующий                  ║
║                                              ║
║ Выберите действие: """)
    try:
        mode = int(mode)
        if mode == 1:
            print("""╔══════════════════════════════════════════════╗
    ║            СОЗДАНИЕ АККАУНТА                 ║
    ╠══════════════════════════════════════════════╣
    ║ Придумайте логин и пароль для нового аккаунта║
    ╚══════════════════════════════════════════════╝""")
            name = input("Введите имя: ")
            pas = input("Введите пароль: ")
            usr.create(name,pas)
        if  mode == 2:
            regis = False
    except:
        print("ошибка")
    
    


continuing = False

print("""╔══════════════════════════════════════════════╗
║               АВТОРИЗАЦИЯ                    ║
╠══════════════════════════════════════════════╣
║ Введите ваши учетные данные для входа        ║
╚══════════════════════════════════════════════╝""")
for i in range(3):
    name = input("Введите имя: ")
    pas = input("Введите пароль: ")
    if usr.validate(name,pas):
        continuing = True
        break 
        
    else:
        continue












os.system('cls' if os.name == 'nt' else 'clear')

while continuing:
    print("╔════════════════════════════════════════════╗")
    print("║           СПИСОК ДЕЛ                       ║")
    print("║     твоя продуктивность  не имеет значение ║")
    print("╠════════════════════════════════════════════╣")
    print("║ [1] ➕ Добавить задачу                        ")
    print("║ [2] ✅ Отметить выполнение                      ")
    print("║ [3] 🗑️  Удалить задачу                        ")
    print("║ [4] 📋 Показать все задачи                   ")
    print("║                                              ")
    print("║ [выход] Закрыть программу                    ")
    print("╠══════════════════════════════════════╣")
    print("║ Количество панических атак у меня за неделю: [########] 10/10 ")
    print(f"║ Количество выполненых тасков у меня за неделю: [{"#"*dec.respect}{"."*(10-dec.respect)}] {dec.respect}/10 ")
    print("╚══════════════════════════════════════╝")


    user_input = input("Ведите режим: ")
    if user_input =="1":
        n = input("Введите количество Задач которе вы введете: ")
        try:
            n = int(n)
            for _ in range(n):
                word = input("Задача: ")
                meaning = input("Текст Задачи: ")
                times = input("Время в формате %H.%M.%d.%m.%Y")
                dec.create(word,meaning,times,usr.currentuser)
        except:
            print("Неправильный ввод начинайте по новой")
    
    
    
    elif user_input.lower() =="выход":
        continuing = False 
    elif user_input == "2":
        print("Id userid NAME TEXT TIME STATUS")
        for el in dec.Read(usr.currentuser):
            print("-".join([str(i) for i in el ]))
        
        user_input = input("номер изменения")
        user_status = input("СТАТУС: ")
        dec.update_task(user_input,user_status,usr.currentuser)
        
    elif user_input == "3":
        
        print(dec.Read(usr.currentuser))
        user_input = input("номер удаления")
        dec.delete(user_input,usr.currentuser)
        
    elif user_input =="4":
        print("Id userid NAME TEXT TIME STATUS")
        for el in dec.Read(usr.currentuser):
            
            print("-".join([str(i) for i in el ]))
        
        inp = input("Введите что то если прочитали")
        os.system('cls' if os.name == 'nt' else 'clear')
    
        
    else:
        print("Пересмотрите свои отношения к вводу комманд")
    
    

