from sqlite3.dbapi2 import Cursor
from tkinter import Entry, Frame, Listbox, Scrollbar, StringVar, Tk, Toplevel, ttk, END, messagebox
from tkinter.constants import ACTIVE, ANCHOR, BOTH, LEFT, RIGHT, SINGLE
import sqlite3
import re
from datetime import datetime

class App:
    def __init__(self, master):
        self.master = master
        master.title("Contact manager")



        self.add_contacts = ttk.Button(self.master, text="Add contact", padding=(10, 5), width=15, command=self.add_contact_fun)
        self.edit_contacts = ttk.Button(self.master, text="Edit contacts", padding=(10, 5), width=15, command=self.edit_contact)
        self.delete_contact = ttk.Button(self.master, text="Delete contact", padding=(10, 5), width=15, command=self.delete_click)


        self.options = ("A-Z", "Z-A", "from oldest", "from newest")
        self.option_var = StringVar(self.master)
        self.filter_contact = ttk.OptionMenu(self.master, self.option_var, self.options[0], *self.options, command=self.refresh_list)

        self.scrollbar = ttk.Scrollbar(self.master)
        self.scrollbar.grid(row=0, column=4)

        self.my_list = Listbox(self.master, yscrollcommand=self.scrollbar.set, width=50, selectmode=SINGLE)

        self.my_list.grid(row=0, column=0, columnspan=3)
        self.scrollbar.config( command = self.my_list.yview)

        self.show_records()



        

        self.search_contact = ttk.Entry(self.master)
        self.show = ttk.Button(self.master, text="Show", padding=(10, 5), width=15)

        self.add_contacts.grid(row=1, column=0, padx=5)
        self.edit_contacts.grid(row=1, column=1, padx=5)
        self.delete_contact.grid(row=1, column=3, padx=5)
        self.filter_contact.grid(row=2, column=0, padx=5)
        self.search_contact.grid(row=2, column=1, padx=5)

        self.search_contact.bind("<KeyRelease>", self.search)


        self.show.grid(row=2, column=3, padx=5)

    def add_contact_fun(self):
        add_window = Toplevel(self.master)
        add = Add(add_window, self.my_list, self.option_var)

        
    def show_records(self):
        order_var = self.option_var.get()
        if order_var == "from oldest":
            conn = sqlite3.connect("Contacts.db")
            cursor = conn.cursor()
            cursor.execute("SELECT rowid, * FROM records ORDER BY rowid")
            records = map(lambda x: " ".join(map(str, x)), cursor.fetchall())   # list of tuples
            conn.commit()
            conn.close()
            for i in records:
                self.my_list.insert(END, str(i))

        if order_var == "A-Z":
            conn = sqlite3.connect("Contacts.db")
            cursor = conn.cursor()
            cursor.execute("SELECT rowid, * FROM records ORDER BY name")
            records = map(lambda x: " ".join(map(str, x)), cursor.fetchall())   # list of tuples
            conn.commit()
            conn.close()
            for i in records:
                self.my_list.insert(END, str(i))

        if order_var == "Z-A":
            conn = sqlite3.connect("Contacts.db")
            cursor = conn.cursor()
            cursor.execute("SELECT rowid, * FROM records ORDER BY name DESC")
            records = map(lambda x: " ".join(map(str, x)), cursor.fetchall())   # list of tuples
            conn.commit()
            conn.close()
            for i in records:
                self.my_list.insert(END, str(i))

        if order_var == "from newest":
            conn = sqlite3.connect("Contacts.db")
            cursor = conn.cursor()
            cursor.execute("SELECT rowid, * FROM records ORDER BY rowid DESC")
            records = map(lambda x: " ".join(map(str, x)), cursor.fetchall())   # list of tuples
            conn.commit()
            conn.close()
            for i in records:
                self.my_list.insert(END, str(i))


        


    
    def edit_contact(self):
        selected_contact = self.my_list.get(ANCHOR)
        edit_window = Toplevel(self.master)
        edit = Edit(edit_window, self.master, selected_contact, self.my_list, self.option_var)

    def refresh_list(self, *args):
        self.my_list.delete(0, END)
        self.show_records()


    def delete_click(self):
        selected_contact = self.my_list.get(ANCHOR)
        selected_contact = selected_contact.split()
        selected_contact = (int(selected_contact[0]), selected_contact[1], selected_contact[2])
        response = messagebox.askquestion("Delete", "Do you want to delete {}?".format(selected_contact[1] + " " + selected_contact[2]))
        if response == "yes":
            id = selected_contact[0]
            conn = sqlite3.connect("Contacts.db")
            cursor = conn.cursor()
            cursor.execute("DELETE from records WHERE rowid=?", (id,))
            conn.commit()
            conn.close()

            self.refresh_list()


    def search(self, event):
        conn = sqlite3.connect("Contacts.db")
        cursor = conn.cursor()
        cursor.execute("SELECT rowid, * FROM records ORDER BY rowid")
        records = map(lambda x: " ".join(map(str, x)), cursor.fetchall())   # list of tuples
        conn.commit()
        conn.close()

        val = event.widget.get()
        if val == '':
            data = records
        else:
            data = []
            for item in records:
                if val.lower() in item.lower():
                    data.append(item)	
        self.update(data)


    def update(self, data):
	    self.my_list.delete(0, 'end')

	    # put new data
	    for item in data:
		    self.my_list.insert('end', item)

    


class Add(App):
    def __init__(self, master, my_list, option_var):
        self.option_var = option_var
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
        if len(self.name_entry.get()) < 1 or len(self.surname_entry.get()) < 1:
            messagebox.showerror("Name and Surname", "Please enter Name and Surname!")
            return None

        for i in str(self.phone_entry.get()):
            if i not in (" ", "+", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                messagebox.showerror("Phone Number", "You can only use '+', spaces and digits!")
                return None

        if len(self.email_entry.get()) > 0:
            self.regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
            if self.check(self.email_entry.get()) == False:
                messagebox.showerror("Email", "Invalid email")
                return None

        if len(str(self.birthday_entry.get())) > 0:
            format = "%d.%m.%Y"
            date = str(self.birthday_entry.get())
            try:
                datetime.strptime(date, format)
            except:
                messagebox.showerror("Birthday", "Invalid birthday format.\nPlease enter day.month.year format without spaces.")
                return None

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

    def check(self, email):
        if(re.search(self.regex, email)):   
            return True
        else:   
            return False


class Edit(App):
    def __init__(self, master, frame, id, my_list, option_var):
        self.option_var = option_var
        self.frame = frame
        self.master = master
        self.id = int(id[0])
        self.my_list = my_list
        master.title("Edit contact")
        
        self.fill()



        self.edit_button = ttk.Button(self.master, text="Edit", command=self.edit_button)
        
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
        cursor.execute("SELECT * FROM records WHERE rowid=?", (self.id,))
        self.records = [i for i in cursor.fetchall()[0]]
        

        self.name_already = self.records[0]
        self.surname_already = self.records[1]
        self.birthday_already = self.records[2]
        self.email_already = self.records[3]
        self.phone_already = self.records[4]
        self.note_already = self.records[5]


    def edit_button(self):
        if len(self.name_entry.get()) < 1 or len(self.surname_entry.get()) < 1:
            messagebox.showerror("Name and Surname", "Please enter Name and Surname!")
            return None

        for i in str(self.phone_entry.get()):
            if i not in (" ", "+", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                messagebox.showerror("Phone", "You can only use '+', spaces and digits!")
                return None

        if len(self.email_entry.get()) > 0:
            self.regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
            if self.check(self.email_entry.get()) == False:
                messagebox.showerror("Email", "Invalid email")
                return None

        if len(str(self.birthday_entry.get())) > 0:
            format = "%d.%m.%Y"
            date = str(self.birthday_entry.get())
            try:
                datetime.strptime(date, format)
            except:
                messagebox.showerror("Birthday", "Invalid birthday format.\nPlease enter day.month.year format without spaces.")
                return None

        conn = sqlite3.connect("Contacts.db")
        cursor = conn.cursor()

        cursor.execute("""UPDATE records SET name=?,
                        surname=?,
                        birthday=?,
                        email=?,
                        phone=?,
                        note=? WHERE rowid=?
                    """,
                    (self.name_entry.get(),
                    self.surname_entry.get(),
                    self.birthday_entry.get(),
                    self.email_entry.get(),
                    self.phone_entry.get(),
                    self.note_entry.get(),
                    self.id))
        conn.commit()
        conn.close()

        self.refresh_list()

        self.master.destroy()    


    def check(self, email):
        if(re.search(self.regex, email)):   
            return True
        else:   
            return False   




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

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()