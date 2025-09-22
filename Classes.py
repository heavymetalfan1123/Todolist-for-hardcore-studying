import time
import csv
def anigilate(date1,date2):
        
        y2 = time.strptime(date2,"%H.%M.%d.%m.%Y")
        
        return time.mktime(y2)-date1   
class Todolist:
    def __init__(self,filename):
        self.filename = filename
        self.NST_arr = []
        self.respect = 0 
        with open(f'{self.filename}.csv',"r+", newline='',encoding='utf-8') as csvfile:
            
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                self.NST_arr.append(row)
    
    def create(self,name,text,time):

        self.NST_arr.append([name,text,time,False])
        self.sync()

    def Read(self):
        return self.NST_arr

    def update_task(self,num_of_change,status):
        #try:
            if  self.NST_arr != [] and int(num_of_change)<=len(self.NST_arr):
                
                    
                    num_of_change = int(num_of_change)
                    num_of_change-=1
                    #print(*self.NST_arr[:num_of_change],*self.NST_arr[num_of_change:])
                    
                    if status.lower() == "true":
                    
                        self.NST_arr[num_of_change][3] = True
                        print(anigilate(time.time(),self.NST_arr[num_of_change][2]))
                        if anigilate(time.time(),self.NST_arr[num_of_change][2]) >0 :

                            self.respect+=1
                        else:
                            self.respect-=1
                        self.NST_arr.pop(num_of_change)
                    else:
                        print("TASK NOT MADE")
                    
                
            else:
                print("ERORRRRRR REMAAAAKEEEE")
        #except:
        #    print("поаккуратней")

            self.sync()

    def delete(self,num_of_change):
        
        if  self.NST_arr != [] and int(num_of_change)<=len(self.NST_arr):
            try:
                    
                num_of_change = int(num_of_change)
                num_of_change-=1
                print(*self.NST_arr[:num_of_change],*self.NST_arr[num_of_change+1:])
                    
                self.NST_arr = self.NST_arr[:num_of_change]+self.NST_arr[num_of_change+1:]
                    
            except:
                print("ХЕЗЕ НУ ОШИБКА")
        else:
            print("ERROR")
        
        self.sync()
    def sync(self):
        # i = 0
        # for el in self.NST_arr:
        #     if True in el:
        #         self.NST_arr.delete(i)
        #     i+=1  

        with open(f"{self.filename}.csv","w", newline="",encoding='utf-8') as newfile:
            writ = csv.writer(newfile)
            for el in self.NST_arr:
                writ.writerow(el)
    
    
