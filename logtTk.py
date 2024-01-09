from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry("500x500")
root.title("Login page")
root.config(bg="#fbfcb5")
root.iconbitmap


fr=Frame(root,width=500,height=50,bg="aqua")
fr.pack(pady=5)

title=Label(fr,text="                          Login                         " ,font=("fantasy",22),fg="#0d0f77",bg="aqua")
title.pack(pady=0)

photo=PhotoImage(file="C:\\Users\\HHSS\\Desktop\\Learn_Python\\Tkinter\\log.png")
res=photo.subsample(10,10)
lbl=Label(root,image=res,bg="#fbfcb5")
lbl.pack(pady=10)

lu=Label (root,text="USERNAME :" ,fg="black",font=("courier",11),bg="#fbfcb5")
lu.pack(pady=5)
user=Entry(root,bg="white",width=30)
user.pack(pady=2)

lu=Label (root,text="PASSWORD :" ,fg="black",font=("courier",11),bg="#fbfcb5")
lu.pack(pady=10)
pas=Entry(root,bg="white",width=30)
pas.pack(pady=2)

bt1=Button(root,text="login",bg="#85f762",width=10)
bt1.pack(pady=10)
bt2=Button(root,text="create new",bg="#6285f7",width=10)
bt2.pack(pady=10)
lu=Label (root,text="Forget your password ? :" ,fg="blue",font=("arial",11),bg="#fbfcb5")
lu.pack(pady=5)
























root.mainloop ()






































































