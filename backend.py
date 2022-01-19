
import sqlite3

def connect():
    con = sqlite3.connect("schools.db")
    cur = con.cursor()
    command_create = "CREATE TABLE IF NOT EXISTS school (id INTEGER PRIMARY KEY,name TEXT ,family Text,age INTEGER,shomare INTEGER)"
    cur.execute(command_create)
    con.commit()
    con.close()
    
def insert(name,family,age,shomare):
    con = sqlite3.connect("schools.db")
    cur = con.cursor()
    command_insert = "INSERT INTO school VALUES(NULL,?,?,?,?)"
    cur.execute(command_insert,(name,family,age,shomare))
    con.commit()
    con.close()

def show_all():
    con = sqlite3.connect("schools.db")
    cur = con.cursor()
    command_show = "SELECT * FROM school"
    cur.execute(command_show)
    row = cur.fetchall()
    con.commit()
    con.close()
    return row

def search(name="",family="",age="",shomare=""):
    con = sqlite3.connect("schools.db")
    cur = con.cursor()
    command_search = ("SELECT * FROM school WHERE name=? OR family=? OR age=? OR shomare=?")
    cur.execute(command_search,(name,family,age,shomare))
    row = cur.fetchall()
    con.commit()
    con.close()
    return row

def delete(id):
    con = sqlite3.connect("schools.db")
    cur = con.cursor()
    command_delete = "DELETE FROM school WHERE id=?"
    cur.execute(command_delete,(id,))
    con.commit()
    con.close()
    
def update(id,name,family,age,shomare):
    con = sqlite3.connect("schools.db")
    cur = con.cursor()
    command_update = "UPDATE school SET name=?,family=?,age=?,shomare=? WHERE id=?"
    cur.execute(command_update,(name,family,age,shomare,id))
    con.commit()
    con.close()    
    

connect()     

#insert("parsa","ahmadi",17,56321) 
#print(show_all())
#print(search("parsa"))
#delete(6)
#update(2,"new name","new family",34,6789)

  
