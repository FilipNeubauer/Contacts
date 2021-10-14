from sqlite3.dbapi2 import Cursor
from tkinter import Entry, Frame, Listbox, Scrollbar, Tk, Toplevel, ttk, END
from tkinter.constants import ACTIVE, ANCHOR, BOTH, LEFT, RIGHT, SINGLE
import sqlite3

class App:
    def __init__(self, master):
        self.master = master
        master.title("Contact manager")

        self.scrollbar = ttk.Scrollbar(self.master)
        self.scrollbar.grid(row=0, column=4)

        self.my_list = Listbox(self.master, yscrollcommand=self.scrollbar.set, width=50, selectmode=SINGLE)

        self.my_list.grid(row=0, column=0, columnspan=3)
        self.scrollbar.config( command = self.my_list.yview)

        self.show_records()


        self.add_contacts = ttk.Button(self.master, text="Add contact", padding=(10, 5), width=15, command=self.add_contact_fun)
        self.edit_contacts = ttk.Button(self.master, text="Edit contacts", padding=(10, 5), width=15, command=self.edit_contact)
        self.delete_contact = ttk.Button(self.master, text="Delete contact", padding=(10, 5), width=15)
        self.filter_contact = ttk.Button(self.master, text="A-Z", padding=(10, 5), width=15)
        self.search_contact = ttk.Entry(self.master)
        self.show = ttk.Button(self.master, text="Show", padding=(10, 5), width=15)

        self.add_contacts.grid(row=1, column=0, padx=5)
        self.edit_contacts.grid(row=1, column=1, padx=5)
        self.delete_contact.grid(row=1, column=3, padx=5)
        self.filter_contact.grid(row=2, column=0, padx=5)
        self.search_contact.grid(row=2, column=1, padx=5)
        self.show.grid(row=2, column=3, padx=5)

    def add_contact_fun(self):
        add_window = Toplevel(self.master)
        add = Add(add_window, self.my_list)

        
    def show_records(self):
        conn = sqlite3.connect("Contacts.db")
        cursor = conn.cursor()
        cursor.execute("SELECT rowid, * FROM records")
        records = map(lambda x: " ".join(map(str, x)), cursor.fetchall())   # list of tuples
        conn.commit()
        conn.close()
        for i in records:
            self.my_list.insert(END, str(i))
        


    
    def edit_contact(self):
        selected_contact = self.my_list.get(ANCHOR)
        print(selected_contact)
        edit_window = Toplevel(self.master)
        edit = Edit(edit_window, self.master, selected_contact)

    def refresh_list(self):
        self.my_list.delete(0, END)
        self.show_records()

        


class Add(App):
    def __init__(self, master, my_list):
        self.my_list = my_list
        self.master = master
        master.title("Add contact")


        self.add_button = ttk.Button(self.master, text="Add", command=self.add_contact)
        
        self.add_button.grid(row=6, column=0, columnspan=2)

        self.name_label = ttk.Label(self.master, text="First name")
        self.surname_label = ttk.Label(self.master, text="Last name")
        self.birthday_label = ttk.Label(self.master, text="Birthday")
        self.email_label = ttk.Label(self.master, text="Email")
        self.phone_label = ttk.Label(self.master, text="Phone number")
        self.note_label = ttk.Label(self.master, text="Note")

        self.name_label.grid(row=0, column=0)
        self.surname_label.grid(row=1, column=0)
        self.birthday_label.grid(row=2, column=0)
        self.email_label.grid(row=3, column=0)
        self.phone_label.grid(row=4, column=0)
        self.note_label.grid(row=5, column=0)

        self.name_entry = ttk.Entry(self.master)
        self.surname_entry = ttk.Entry(self.master)
        self.birthday_entry = ttk.Entry(self.master)
        self.email_entry = ttk.Entry(self.master)
        self.phone_entry = ttk.Entry(self.master)
        self.note_entry = ttk.Entry(self.master)

        self.name_entry.grid(row=0, column=1)
        self.surname_entry.grid(row=1, column=1)
        self.birthday_entry.grid(row=2, column=1)
        self.email_entry.grid(row=3, column=1)
        self.phone_entry.grid(row=4, column=1)
        self.note_entry.grid(row=5, column=1)

    def add_contact(self):
        conn = sqlite3.connect("Contacts.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO records VALUES (?, ?, ?, ?, ?, ?)", 
                    (self.name_entry.get(),
                    self.surname_entry.get(),
                    self.birthday_entry.get(),
                    self.email_entry.get(),
                    self.phone_entry.get(),
                    self.note_entry.get()))
        conn.commit()
        conn.close()

        self.refresh_list()

        self.master.destroy()


class Edit(App):
    def __init__(self, master, frame, record):
        self.frame = frame
        self.master = master
        self.record = int(record[0])
        master.title("Edit contact")
        
        self.fill()



        self.edit_button = ttk.Button(self.master, text="Edit")
        
        self.edit_button.grid(row=6, column=0, columnspan=2)

        self.name_label = ttk.Label(self.master, text="First name")
        self.surname_label = ttk.Label(self.master, text="Last name")
        self.birthday_label = ttk.Label(self.master, text="Birthday")
        self.email_label = ttk.Label(self.master, text="Email")
        self.phone_label = ttk.Label(self.master, text="Phone number")
        self.note_label = ttk.Label(self.master, text="Note")

        self.name_label.grid(row=0, column=0)
        self.surname_label.grid(row=1, column=0)
        self.birthday_label.grid(row=2, column=0)
        self.email_label.grid(row=3, column=0)
        self.phone_label.grid(row=4, column=0)
        self.note_label.grid(row=5, column=0)

        self.name_entry = ttk.Entry(self.master, )
        self.surname_entry = ttk.Entry(self.master)
        self.birthday_entry = ttk.Entry(self.master)
        self.email_entry = ttk.Entry(self.master)
        self.phone_entry = ttk.Entry(self.master)
        self.note_entry = ttk.Entry(self.master)

        self.name_entry.insert(0, self.name_already)
        self.surname_entry.insert(0, self.surname_already)
        self.birthday_entry.insert(0, self.birthday_already)
        self.email_entry.insert(0, self.email_already)
        self.phone_entry.insert(0, self.phone_already)
        self.note_entry.insert(0, self.note_already)


        self.name_entry.grid(row=0, column=1)
        self.surname_entry.grid(row=1, column=1)
        self.birthday_entry.grid(row=2, column=1)
        self.email_entry.grid(row=3, column=1)
        self.phone_entry.grid(row=4, column=1)
        self.note_entry.grid(row=5, column=1)


    def fill(self):
        conn = sqlite3.connect("Contacts.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM records WHERE rowid=?", (self.record,))
        self.records = [i for i in cursor.fetchall()[0]]
        

        self.name_already = self.records[0]
        self.surname_already = self.records[1]
        self.birthday_already = self.records[2]
        self.email_already = self.records[3]
        self.phone_already = self.records[4]
        self.note_already = self.records[5]




# conn = sqlite3.connect("Contacts.db")
# cursor = conn.cursor()

# cursor.execute("""CREATE TABLE records (
#             name text,
#             surname text,
#             birthday text,
#             email text,
#             phone text,
#             note text
# )""")

# conn.commit()
# conn.close()
        
root = Tk()
app = App(root)
root.mainloop()