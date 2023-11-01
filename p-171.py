from tkinter import *
from PIL import ImageTk , Image
from datetime import datetime
import pytz 
import time

root = Tk()
root.title("World CLock")
root.geometry("600x600")

india_map = ImageTk.PhotoImage(Image.open("india.jpg"))
usa_map = ImageTk.PhotoImage(Image.open("usa.png"))
australia_map = ImageTk.PhotoImage(Image.open("australia.jpg"))
japan_map = ImageTk.PhotoImage(Image.open("japan.jpeg"))
    
india_label = Label(root , text = "India")
india_label.place(relx = 0.3 , rely = 0.1 , anchor = CENTER)

india_pm = Label(root)
india_pm["image"] = india_map
india_pm.place(relx = 0.3 , rely = 0.2 , anchor = CENTER)

india_time = Label(root)
india_time.place(relx = 0.3 , rely = 0.3 , anchor = CENTER)



usa_label = Label(root , text = "USA")
usa_label.place(relx = 0.6 , rely = 0.1 , anchor = CENTER)

usa_pm = Label(root)
usa_pm["image"] = usa_map
usa_pm.place(relx = 0.6 , rely = 0.2 , anchor = CENTER)

usa_time = Label(root)
usa_time.place(relx = 0.6 , rely = 0.3 , anchor = CENTER)


australia_label = Label(root , text = "Australia")
australia_label.place(relx = 0.6 , rely = 0.1 , anchor = CENTER)

australia_pm = Label(root)
australia_pm["image"] = australia_map
australia_pm.place(relx = 0.6 , rely = 0.2 , anchor = CENTER)

australia_time = Label(root)
australia_time.place(relx = 0.6 , rely = 0.3 , anchor = CENTER)



japan_label = Label(root , text = "Japan")
japan_label.place(relx = 0.6 , rely = 0.1 , anchor = CENTER)

japan_pm = Label(root)
japan_pm["text"] = japan_map
japan_pm.place(relx = 0.6 , rely = 0.2 , anchor = CENTER)

japan_time = Label(root)
japan_time.place(relx = 0.6 , rely = 0.3 , anchor = CENTER)



class India():
    
    def time(self):
        home = pytz.timezone('Asia/Kolkata')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H : %M : %S")
        india_time["text"] = "Time : " + current_time
        india_time.after(200,self.time)
        
class USA():
    
    def time(self):
        home = pytz.timezone('US/Central')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H : %M : %S")
        usa_time["text"] = "Time : " + current_time
        usa_time.after(200,self.time)
        
class Japan():
    
    def time(self):
        home = pytz.timezone('Japan')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H : %M : %S")
        japan_time["text"] = "Time : " + current_time
        japan_time.after(200,self.time)
        
        
class Australia():
    
    def time(self):
        home = pytz.timezone('Australia/ACT')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H : %M : %S")
        australia_time["text"] = "Time : " + current_time
        australia_time.after(200,self.time)
        
        
obj_india = India()        
obj_australia = Australia()        
obj_usa = USA()        
obj_japan = Japan()

india_btn = Button(root,text = "Show Time" , command = obj_india.time)
india_btn.place(relx = 0.3 , rely = 0.4 , anchor = CENTER)

australia_btn = Button(root , text = "Show Time " , command = obj_australia.time)
australia_btn.place(relx = 0.3 , rely = 0.9 , anchor = CENTER)

usa_btn = Button(root, text = "Show TIme " , command = obj_usa.time)
usa_btn.place(relx = 0.6 , rely = 0.4 , anchor = CENTER)

japan_btn = Button(root ,text = "Show Time" , command = obj_japan.time)
japan_btn.place(relx = 0.6 , rely = 0.9 , anchor = CENTER)


root.mainloop()














