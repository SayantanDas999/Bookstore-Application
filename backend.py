# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 01:13:12 2019

@author: Sayantan
"""

import sqlite3

def connect():
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()
    
def insert(title,author,year,isbn):
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("SELECT * from book")
    results=cur.fetchall()
    conn.close()
    return results
    
def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("SELECT * from book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    results=cur.fetchall()
    conn.close()
    return results
    
def delete(id):
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()
    
def update(id,title,author,year,isbn):
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
#insert("The Earth","John Smith",1967,176980)
#delete(4)
#update(3,"The Moon", "Jaby Koay",2007,345228)
#print(view())
#print(search(author="John Smith"))


