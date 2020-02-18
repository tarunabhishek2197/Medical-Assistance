from tkinter import *
from tkinter import messagebox
import sqlite3 as s
import requests as r
import bs4
global cu
try:
    client=s.connect("D:\\daru.db")
    cu=client.cursor()
    cu.execute("create table Collection9(name varchar(20),email varchar(50),mobile int,username varchar(50) PRIMARY KEY,password varchar(50))")
except:
    pass

def login():
    try:
        global scr1
        scr1.destroy()
    except:
        pass
    global scr
    scr=Tk()
    scr.title('Login Page')
    scr.geometry("300x300")
    scr.config(bg='yellow')
    l=Label(scr,text='LOGIN PAGE',font=('times',20,'bold'),fg='black',bg='blue')
    l.pack(side=TOP,fill=X)
    l=Label(scr,text='USER NAME',font=('times',12,'bold'),fg='black',bg='red')
    l.place(x=30,y=80)
    l=Label(scr,text='PASSWORD',font=('times',12,'bold'),fg='black',bg='red')
    l.place(x=30,y=140)
    global e,e1
    e=Entry(scr)
    e.place(x=160,y=80)
    e1=Entry(scr)
    e1.place(x=160,y=140)
    b=Button(scr,text='LOGIN',bg='red',fg='black',command=check)
    b.place(x=60,y=200)
    b1=Button(scr,text='REGISTER',bg='red',fg='black',command=register)
    b1.place(x=150,y=200)    
    scr.mainloop()

def check():
    global e,e1,cu
    cu.execute("select count(*) from Collection9 where username=%r and password=%r"%(e.get(),e1.get()))
    a=cu.fetchall()
    b=a[0][0]
    if b==1:
        main()
    else:
        global scr
        scr.destroy()
        login()

def scrap():
    global lst,eee
    lst=[]
    dt=r.request('get','https://www.1mg.com/search/all?name=%r'%(eee.get()))
    s=bs4.BeautifulSoup(dt.text,'html.parser')
    for i in s.findAll('div'):
        if i.get('class'):
            if len([x for x in i.get('class') if 'style__container__' in x])>0:
                if i.find('a'):
                    x=i.find('a')
                    try:
                        dts=r.request('get','https://www.1mg.com'+x.get('href'))
                        s1=bs4.BeautifulSoup(dts.text,'html.parser')
                        for j in s1.findAll('div'):
                            if j.get('class'):
                                if len([x for x in j.get('class') if '_product-description' in x])>0:
                                    try:
                                        lst.append(j.text)
                                    except:
                                        pass
                                elif  len([x for x in j.get('class') if 'DrugOverview__container' in x])>0:
                                    try:
                                       lst.append(j.text)
                                    except:
                                        pass
                    except:
                        pass
        global data,m
        data=iter(lst)
        
def nxt():
    global data,m
    try:
        m.config(text=next(data))
    except:
        m.config(text='The End')
        
            
def main():
    global scr
    scr.destroy()
    global scr2
    scr2=Tk()
    scr2.title("MAIN")
    scr2.geometry("300x300")
    global eee
    eee=Entry(scr2)
    eee.place(x=80,y=80)
    b=Button(scr2,text='GO',bg='red',fg='black',command=scrap)
    b.place(x=100,y=200)
    global m
    m=Message(scr2)
    m.pack()
    bbb=Button(scr2,text='Next',command=nxt)
    bbb.pack()
    scr2.mainloop()

def fun():
    global e1,e2,e3,e4,e5
    cu.execute("insert into Collection9 values(%r,%r,%d,%r,%r)"%(e1.get(),e2.get(),int(e3.get()),e4.get(),e5.get()))
    client.commit()
    messagebox.showinfo("Register","Registration Successfull")
    login()
    
def register():
    global scr
    scr.destroy()
    global scr1,e1,e2,e3,e4,e5
    scr1=Tk()
    scr1.title('SIGN UP')
    scr1.geometry("500x1000")
    scr1.config(bg='cornsilk3')
    l=Label(scr1,text='SIGN UP',font=('times',20,'bold'),fg='black',bg='red')
    l.pack(side=TOP,fill=X)
    l1=Label(scr1,text='NAME',font=('times',12,'bold'),fg='black',bg="cornsilk3")
    l1.place(x=60,y=80)
    l2=Label(scr1,text='E-MAIL',font=('times',12,'bold'),fg='black',bg="cornsilk3")
    l2.place(x=60,y=180)
    l3=Label(scr1,text='MOBILE NO',font=('times',12,'bold'),fg='black',bg="cornsilk3")
    l3.place(x=60,y=280)
    l4=Label(scr1,text='USER NAME',font=('times',12,'bold'),fg='black',bg="cornsilk3")
    l4.place(x=60,y=380)
    l5=Label(scr1,text='PASSWORD',font=('times',12,'bold'),fg='black',bg="cornsilk3")
    l5.place(x=60,y=480)
    l6=Label(scr1,text='DOB',font=('times',12,'bold'),fg='black',bg="cornsilk3")
    l6.place(x=60,y=580)

    e1=Entry(scr1)
    e1.place(x=200,y=80)
    e2=Entry(scr1)
    e2.place(x=200,y=180)
    e3=Entry(scr1)
    e3.place(x=200,y=280)
    e4=Entry(scr1)
    e4.place(x=200,y=380)
    e5=Entry(scr1)
    e5.place(x=200,y=480)
    e6=Entry(scr1)
    e6.place(x=200,y=580)
    b=Button(scr1,text='SUBMIT',bg='red',fg='black',command=fun)
    b.place(x=200,y=640)
    b1=Button(scr1,text='Back_To_Login',bg='green',fg="black",command=login)
    b1.place(x=300,y=640)
    scr1.mainloop()

    

login()    
    
