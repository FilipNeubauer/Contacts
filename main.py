from tkinter import Frame, Listbox, Scrollbar, Tk, ttk, END
from tkinter.constants import BOTH, LEFT, RIGHT
import sqlite3

class App(Tk):
    def __init__(self):
        super().__init__()
        






        frame = ttk.Frame(self)
        frame.grid(row=0, column=0, columnspan=4)

        idk_list = [i for i in range(9)]

        self.scrollbar = ttk.Scrollbar(frame)
        self.scrollbar.pack(side=RIGHT)

        my_list = Listbox(frame, yscrollcommand=self.scrollbar.set, width=50)
        for i in idk_list:
            my_list.insert(END, "" + str(i))
        my_list.pack()
        self.scrollbar.config( command = my_list.yview)


        self.add_contacts = ttk.Button(self, text="Add contact", padding=(10, 5), width=15)
        self.edit_contacts = ttk.Button(self, text="Edit contacts", padding=(10, 5), width=15)
        self.delete_contact = ttk.Button(self, text="Delete contact", padding=(10, 5), width=15)
        self.filter_contact = ttk.Button(self, text="A-Z", padding=(10, 5), width=15)
        self.search_contact = ttk.Entry(self)
        self.show = ttk.Button(self, text="Show", padding=(10, 5), width=15)

        self.add_contacts.grid(row=1, column=0, padx=5)
        self.edit_contacts.grid(row=1, column=1, padx=5)
        self.delete_contact.grid(row=1, column=3, padx=5)
        self.filter_contact.grid(row=2, column=0, padx=5)
        self.search_contact.grid(row=2, column=1, padx=5)
        self.show.grid(row=2, column=3, padx=5)


app = App()
app.mainloop()