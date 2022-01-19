from tkinter import *
import backend
win = Tk()
win.geometry("400x400")
win.title("SchoolManagement")

def fill_list(school_info):
    for schools in school_info:
        list_box.insert(END,schools)

def clear_list():
    list_box.delete(0,END)
    

#--------NameInformation--------#
name_label = Label(win,text="name")
name_label.place(x=0,y=0)
name_entry = Entry(win)
name_entry.place(x=45,y=0)
#-------------------#

#--------FamilyInformation--------#
family_name = Label(win,text="family")
family_name.place(x=200,y=0)
family_entry = Entry(win)
family_entry.place(x=245,y=0)
#-------------------#

#--------AgeInformation--------#
age_label = Label(win,text="age")
age_label.place(x=0,y=30)
age_entry = Entry(win)
age_entry.place(x=45,y=30)
#-------------------#

#------------ShenasnameInformation-----------#
shomare_shenasname_label = Label(win,text="shomare")
shomare_shenasname_label.place(x=190,y=30)
shomare_shenasname_entry = Entry(win)
shomare_shenasname_entry.place(x=245,y=30)
#-------------------#

#----------Listbox and Scrollbar--------#
list_box = Listbox(win,width=35,height=10)
list_box.place(x=0,y=70)
scrol_bar = Scrollbar(win)
scrol_bar.place(x=215,y=70)
scrol_bar.config(command=list_box.yview)
list_box.config(yscrollcommand=scrol_bar.set)

def row_selected(event):
    global selected_students
    if len(list_box.curselection()) > 0:
        index = list_box.curselection()[0]
        selected_students = list_box.get(index)
        name_entry.delete(0,END)
        name_entry.insert(END,selected_students[1])
        family_entry.delete(0,END)
        family_entry.insert(END,selected_students[2])
        age_entry.delete(0,END)
        age_entry.insert(END,selected_students[3])
        shomare_shenasname_entry.delete(0,END)
        shomare_shenasname_entry.insert(END,selected_students[4])
    
    

list_box.bind("<<ListboxSelect>>",func=row_selected)
#------------------#

#------------Buttons---------#

def show_information():
    clear_list()
    school_info = backend.show_all()
    fill_list(school_info)
    
    
btn_all_info = Button(win,text="Show All",width=10,command=show_information)
btn_all_info.place(x=300,y=70)

def search_command():
    clear_list()
    school = backend.search(name_entry.get(),family_entry.get(),age_entry.get(),shomare_shenasname_entry.get())
    fill_list(school)  
btn_search = Button(win,text="Search",width=10,command=search_command)
btn_search.place(x=300,y=96)

def add_student():
    backend.insert(name_entry.get(),family_entry.get(),age_entry.get(),shomare_shenasname_entry.get())
    show_information()  
    
btn_add = Button(win,text="Add Student",width=10,command=add_student)
btn_add.place(x=300,y=122)
 
def update():
    backend.update(selected_students[0],name_entry.get(),family_entry.get(),age_entry.get(),shomare_shenasname_entry.get()) 
    show_information()

btn_update = Button(win,text="Update",width=10,command=update)
btn_update.place(x=300,y=148)

def delete():
    backend.delete(selected_students[0])
    show_information()

btn_delete = Button(win,text="Delete",width=10,command=delete)
btn_delete.place(x=300,y=174)

btn_close = Button(win,text="Close",width=10)
btn_close.place(x=300,y=200)

show_information()
win.mainloop()