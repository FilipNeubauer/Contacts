from tkinter import Entry, Frame, Listbox, Scrollbar, Tk, Toplevel, ttk, END
from tkinter.constants import BOTH, LEFT, RIGHT
import sqlite3

class App:
    def __init__(self, master):
        self.master = master
        master.title("Contact manager")

        frame = ttk.Frame(self.master)
        frame.grid(row=0, column=0, columnspan=4)

        idk_list = [i for i in range(9)]

        self.scrollbar = ttk.Scrollbar(frame)
        self.scrollbar.pack(side=RIGHT)

        my_list = Listbox(frame, yscrollcommand=self.scrollbar.set, width=50)
        for i in idk_list:
            my_list.insert(END, "" + str(i))
        my_list.pack()
        self.scrollbar.config( command = my_list.yview)


        self.add_contacts = ttk.Button(self.master, text="Add contact", padding=(10, 5), width=15, command=self.add_contact_fun)
        self.edit_contacts = ttk.Button(self.master, text="Edit contacts", padding=(10, 5), width=15)
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
        self.add_window = Toplevel(self.master)
        self.add = Add(self.add_window)



class Add(App):
    def __init__(self, master):
        self.master = master
        master.title("Add contact")

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







        #self.name_entry = ttk.Entry(self.master)


    
        
root = Tk()
app = App(root)
root.mainloop()