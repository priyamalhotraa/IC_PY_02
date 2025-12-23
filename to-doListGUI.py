import tkinter as tk
import sqlite3

conn = sqlite3.connect("tasks.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS tasks (task TEXT)")
conn.commit()

root=tk.Tk()
root.geometry("600x400")
root.title("To-Do List")

def add_command():
    task=ent.get()
    lbox.insert(tk.END,task)
    ent.delete(0,tk.END)

    cur.execute("INSERT INTO tasks VALUES (?)", (task,))
    conn.commit()

def mark_command():
    pos=lbox.curselection()[0]
    text=lbox.get(pos)
    lbox.delete(pos)
    new_text=f"{text} \u2713"
    lbox.insert(tk.END,new_text)

    cur.execute("DELETE FROM tasks WHERE task=?",(text,))
    cur.execute("INSERT INTO tasks VALUES(?)",(new_text,))
    conn.commit()

def del_command():
    pos = lbox.curselection()[0]
    text=lbox.get(pos)
    lbox.delete(pos)

    cur.execute("DELETE FROM tasks WHERE task=?",(text,))
    conn.commit()

lb1=tk.Label(root,text="Enter task: ", font=('calibri',15))
lb1.place(x=10,y=15)

ent=tk.Entry(root,width=50)
ent.place(x=120,y=20)

lbox=tk.Listbox(root,width=50,height=10)
lbox.place(x=120,y=70)

btn1=tk.Button(root,text="ADD", font=('calibri',15), width=15,command=add_command)
btn1.place(x=50,y=250)

btn2=tk.Button(root,text="MARK", font=('calibri',15), width=15,command=mark_command)
btn2.place(x=230,y=250)

btn3=tk.Button(root,text="REMOVE", font=('calibri',15), width=15,command=del_command)
btn3.place(x=400,y=250)

cur.execute("SELECT task FROM tasks ")
for row in cur.fetchall():
    lbox.insert(tk.END,row[0])

def on_close():
    conn.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW",on_close)

root.mainloop()