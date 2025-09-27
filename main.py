
import os

import time

import os 
import sqlite3








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
                    name TEXT,
                    pas TEXT
                    
                    )
                    
                    """)

        self.cursr.execute("""CREATE TABLE IF NOT EXISTS tasks 
                    (id INTEGER PRIMARY KEY,
                        userid INTEGER,
                        name TEXT,
                        text TEXT,
                        time TEXT,
                        status BOOL,
                        FOREIGN KEY (userid) REFERENCES users (id)
                    )""")
        # Эта строчка кода заменяется на cursore.execute
        
        self.connect.commit()
    def create(self,name,text,time,userid):
        # Эта строчка заменяется на insert 
        self.cursr.execute("""SELECT * FROM tasks""")
        result = self.cursr.fetchall()
        print(len(result))
        self.cursr.execute(f"""INSERT INTO tasks (id,userid,name,text,time,Status) VALUES({len(result)+1},'{userid}','{name}','{text}','{time}',false)  """)
        #self.cursr.fetchall
        self.sync()

    def Read(self,id):
        # эта строчка заменяется на select 
        self.cursr.execute(f"""SELECT * FROM tasks WHERE userid = {id}
                    """)
        return self.cursr.fetchall()

    def update_task(self,num_of_change,status,usrid):
        # ВОТ ЭТО Я ХЕЗЕ КАК ЗАМЕНИТЬ 
        try:
            

                    
            num_of_change = int(num_of_change)
            self.cursr.execute(f"""UPDATE tasks SET status={status} WHERE id = {num_of_change} AND userid = {usrid}
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

    def delete(self,num_of_change,usrid):
        
        try:
            

                    
            num_of_change = int(num_of_change)
            self.cursr.execute(f"""DELETE FROM tasks WHERE id={num_of_change} AND userid = {usrid}
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
        
        #self.sync()
    def sync(self):
        self.connect.commit()
    
class User:
    
    def __init__(self,filename):
        self.filename = filename
       
        self.curusr = 0 
        self.connect = sqlite3.connect(f"{self.filename}.db")

        self.cursr = self.connect.cursor()
        
        #self.connect.commit()
        self.cursr.execute(f"""SELECT * FROM users """)
        res = self.cursr.fetchall()
        #print(res[0])
        if len(res) <= 0 :
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
        print(res)
        if len(res):
            self.curusr = res[0][0]
            return True 
        else: return False 
    def create(self,name,text):
        # Эта строчка заменяется на insert 

        self.cursr.execute("""SELECT * FROM users""")
        result = self.cursr.fetchall()
        #print(len(result))
        self.cursr.execute(f"""INSERT INTO users (id,name,pas) VALUES({len(result)+1},'{name}','{text}')  """)
        self.curusr = len(result)+1
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
    #try:
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
    # except:
    #     print("Delete this programm")


continuing = True

print("""╔══════════════════════════════════════════════╗
║               АВТОРИЗАЦИЯ                    ║
╠══════════════════════════════════════════════╣
║ Введите ваши учетные данные для входа        ║
╚══════════════════════════════════════════════╝""")
for i in range(3):
    name = input("Введите имя: ")
    pas = input("Введите пароль: ")
    if usr.validate(name,pas):
        break 
        
    else:
        continuing = False 













    #for i in open_file(filename):
    #print(words_arr)
#print("|ДОБРО ПОЖАЛОВАТЬ В АНКИ ДЛЯ БЕДНЫХ|\n|КРАТКАЯ НАВИГАЦИЯ ПО КОМАНДАМ|\n|(1)запись - запись значений (1)   |\n|(2)запоминание - режим запоминания(2)|\n|(3)вывод - вывод словаря в формате Слово-значение-контекст(3)  |\n|выход - выход из програмы     |")

os.system('cls' if os.name == 'nt' else 'clear')

while continuing:
    #os.system('cls' if os.name == 'nt' else 'clear')
    #print("|ДОБРО ПОЖАЛОВАТЬ В АНКИ ДЛЯ БЕДНЫХ|\n|КРАТКАЯ НАВИГАЦИЯ ПО КОМАНДАМ|\n|(1)запись - запись значений (1)   |\n|(2)запоминание - режим запоминания(2)|\n|(3)вывод - вывод словаря в формате Слово-значение-контекст(3)  |\n| (4) очистка файла      |\n|(5) перезапись слова |\n   \n|выход - выход из програмы     |")
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
        n = input("Введите количество слов которе вы введете: ")
        try:
            n = int(n)
            for _ in range(n):
                word = input("Слово:")
                meaning = input("Значение:")
                times = input("Время в формате %H.%M.%d.%m.%Y")
                dec.create(word,meaning,times,usr.curusr)
        except:
            print("Неправильный ввод начинайте по новой")
    
    
    
    elif user_input.lower() =="выход":
        continuing = False 
    elif user_input == "2":
        print("Id userid NAME TEXT TIME STATUS")
        for el in dec.Read(usr.curusr):
            print("-".join([str(i) for i in el ]))
        #if dec.NST_arr !=[]:
        user_input = input("номер изменения")
        user_status = input("СТАТУС: ")
        dec.update_task(user_input,user_status,usr.curusr)
        #else:
        #    print("=ОШИБКА ФАЙЛ ПУСТОЙ=")
    elif user_input == "3":
        #print(dec.words_array)
        print(dec.Read(usr.curusr))
        user_input = input("номер удаления")
        dec.delete(user_input,usr.curusr)
        
    elif user_input =="4":
        print("Id userid NAME TEXT TIME STATUS")
        for el in dec.Read(usr.curusr):
            #for xd in el:
            print("-".join([str(i) for i in el ]))
        #print(dec.Read(usr.curusr))
        inp = input("Введите что то если прочитали")
        os.system('cls' if os.name == 'nt' else 'clear')
    
        
    else:
        print("Пересмотрите свои отношения к вводу комманд")
    #print(dec.respect)
    

