# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 22:16:36 2019

@author: Sayantan
"""

from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index = l1.curselection()[0]
        selected_tuple = l1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass
    

def view_command():
    l1.delete(0,END)
    for row in backend.view():
        l1.insert(END,row)
        
def search_command():
    l1.delete(0,END)
    for row in backend.search(title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get()):
        l1.insert(END,row)
        
def add_command():
    l1.delete(0,END)
    backend.insert(title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get())
    l1.insert(END,(title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get()))
    
def update_command():
    l1.delete(0,END)
    backend.update(selected_tuple[0],title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get())
    
def delete_command():
    l1.delete(0,END)
    backend.delete(selected_tuple[0])

window=Tk()

window.wm_title("BookStore")

t1=Label(window,text="Title")
t1.grid(row=0,column=0)

t2=Label(window,text="Author")
t2.grid(row=0,column=2)

t3=Label(window,text="Year")
t3.grid(row=1,column=0)

t4=Label(window,text="ISBN")
t4.grid(row=1,column=2)

title_entry=StringVar()
e1=Entry(window,textvariable=title_entry)
e1.grid(row=0,column=1)

author_entry=StringVar()
e2=Entry(window,textvariable=author_entry)
e2.grid(row=0,column=3)

year_entry=StringVar()
e3=Entry(window,textvariable=year_entry)
e3.grid(row=1,column=1)

isbn_entry=StringVar()
e4=Entry(window,textvariable=isbn_entry)
e4.grid(row=1,column=3)

l1=Listbox(window,height=6,width=35)
l1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

l1.configure(yscrollcommand=sb1.set)
sb1.configure(command=l1.yview)

l1.bind("<<ListboxSelect>>",get_selected_row)

b1=Button(window,text="View All",width=10,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=10,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=10,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",width=10,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete",width=10,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=10,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()