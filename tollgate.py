from tkinter import *
import datetime as dt
import xlrd
from xlutils.copy import copy
from tkinter import messagebox


def gettime():
    ct=str(dt.datetime.now())
    date=ct[0:10]
    time=ct[11:19]
    return date,time
date,time=gettime()
amt=str(0)

wb=xlrd.open_workbook('Vehicle details.xls')
sh1=wb.sheet_by_index(0)
sh2=wb.sheet_by_index(1)
nc=sh2.ncols
nr=sh2.nrows
pw0=sh1.col_values(0)
pw1=sh1.col_values(1)
pw2=sh1.col_values(2)

print(pw0)
print(pw1)
print(pw2)

nwb=copy(wb)
sh=nwb.get_sheet(1)
nwb.save('Vehicle details.xls')

global g
g=''
def pchange():
    global g,ind
    g=v.get()
    date,time=gettime()
    datev.set(date)
    timev.set(time)
    if len(g)!=0:
        print('value of g is ',g)
        res=g in pw0
        if (res==True):
            ind=pw0.index(g)
            print('your paid amount is ',pw1[ind])
            tripdata=tv.get()
            if(tripdata==1):
                amtv.set(str(pw1[ind]))
            elif(tripdata==2):
                amtv.set(str(pw2[ind]))
    else:
        messagebox.showwarning('Vehicle Entry Status','Choose any vehicle category')
def reset():
    cn=e1.get()
    amtv.set('0')
    tv.set(1)
    e1.delete(0,len(cn))
    v.set(vc[0])
    date,time=gettime()
    datev.set(date)
    timev.set(time)



def totalcollection():
    wb=xlrd.open_workbook('Vehicle details.xls')
    sh2=wb.sheet_by_index(1)
    tcc=sh2.col_values(7)
    messagebox.showinfo('Total collection','total collection today '+str(sum(tcc[2:])))

def call(*vc):
    pchange()
        
        
def submit():
    global g,ind,nr
    if len(g)!=0:
        cn=e1.get()
        tripdata=tv.get()
        print(cn)
        if len(cn)!=0:
            sh.write(nr,0,nr)
            sh.write(nr,1,g)
            sh.write(nr,2,cn)
            sh.write(nr,3,time)
            sh.write(nr,4,date)
            sh.write(nr,5,tripdata)
            sh.write(nr,6,'NHTS001')
            if(tripdata==1):
                sh.write(nr,7,pw1[ind])
            elif(tripdata==2):
                sh.write(nr,7,pw2[ind])
            nr=nr+1
            reset()
            messagebox.showinfo('Payment Status','data submission successful')

            nwb.save('Vehicle details.xls')
            reset()
        else:
            messagebox.showwarning('Vehicle Entry Status','please enter vehicle number')

    else:
        messagebox.showwarning('Vehicle Entry Status','Choose any vehicle category')
        

root=Tk()
root.title('NH TOLL COLLECTION SYSTEM')
root.geometry('800x500')
vc=['Choose vehicle','Car','Truck','Bus','HV']
f1=Frame(root,bg='lightgray',width=750,height=300)
tv=IntVar()

amtv=StringVar()
timev=StringVar()
datev=StringVar()
tv.set(1)
v=StringVar(f1)
v.set(vc[0])
op=OptionMenu(f1,v,*vc)
op.config(bg='lightgray')

l1=Label(f1,text='National Highway toll system',bg='lightgray')
l2=Label(f1,text='Vehicle No',bg='lightgray')
l3=Label(f1,text='Time : ',bg='lightgray')
l4=Label(f1,textvariable=timev,bg='gray',width=8)
timev.set(time)
l5=Label(f1,text='Date : ',bg='lightgray')
l6=Label(f1,textvariable=datev,bg='gray',width=9)
datev.set(date)
l7=Label(f1,text='Amount Paid: ',bg='lightgray')
l8=Label(f1,textvariable=amtv,bg='gray',width=9)
amtv.set('0')
e1=Entry(f1,width=20)
f2=Frame(f1,bg='gray',width=220,height=60)
r1=Radiobutton(f2,text='One way',variable=tv,value=1,command=pchange)
r2=Radiobutton(f2,text='Round Trip',variable=tv,value=2,command=pchange)
b1=Button(root,text='Submit Entry',command=submit)
b2=Button(root,text='Total Collection Today',command=totalcollection)
v.trace('w',call)




f1.place(x=25,y=25)
l1.place(x=300,y=10)
op.place(x=10,y=100)
l2.place(x=300,y=100)
l3.place(x=600,y=50)
l4.place(x=650,y=50)
l5.place(x=600,y=20)
l6.place(x=650,y=20)
l7.place(x=550,y=250)
l8.place(x=650,y=250)
e1.place(x=400,y=100)
f2.place(x=100,y=200)
r1.place(x=10,y=20)
r2.place(x=110,y=20)
b1.place(x=600,y=400)
b2.place(x=50,y=400)

root.mainloop()

