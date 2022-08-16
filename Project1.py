import sqlite3
import tkinter
import tkinter.messagebox

#define connection and cursor

conn = sqlite3.connect('student_attendance.db')

c = conn.cursor()

# create students table

c.execute('''CREATE TABLE IF NOT EXISTS
students(student_id INTEGER PRIMARY KEY, name TEXT, number INTEGER, attendance_percentage FLOAT, eligibility  TEXT)''')

# Save (commit) the changes
conn.commit()

lists = []

class My_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.mainlabel_frame = tkinter.Frame(self.main_window)
        self.mainbutton_frame = tkinter.Frame(self.main_window)

        self.main_label = tkinter.Label(self.main_window, text='Welcome to the Student Attendance Program!\n' + '_______________________')
        self.display_button = tkinter.Button(self.main_window, text='Display Attendance', command=self.display)
        self.mark_button = tkinter.Button(self.main_window, text='Mark Attendance', command=self.mark)
        self.add_button = tkinter.Button(self.main_window, text='Add Record', command=self.add)
        self.delete_button = tkinter.Button(self.main_window, text='Delete Record', command=self.delete)
        self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)
        
        self.main_label.pack()
        self.display_button.pack()
        self.mark_button.pack()
        self.add_button.pack()
        self.delete_button.pack()
        self.quit_button.pack()

        self.mainlabel_frame.pack()
        self.mainbutton_frame.pack()

    def display(self):
        self.display_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.display_window)
        self.middle_frame = tkinter.Frame(self.display_window)
        self.bottom_frame = tkinter.Frame(self.display_window)

        self.top_label = tkinter.Label(self.top_frame, text='Student Attendance\n' +'_______________' )
        
        self.top_label.pack()
        
        
        for row in c.execute('SELECT student_id, name, attendance_percentage, eligibility  FROM students ORDER BY name'):
            self.info_label = tkinter.Label(self.middle_frame, text=row)
            self.info_label.pack()

        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.display_window.destroy)
        self.quit_button.pack()
        
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def add(self):
        self.add_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.add_window)
        self.entry_frame = tkinter.Frame(self.add_window)
        self.id_frame = tkinter.Frame(self.add_window)
        self.enterbut_frame = tkinter.Frame(self.add_window)
        self.n_frame = tkinter.Frame(self.add_window)

        self.top_label = tkinter.Label(self.top_frame, text='Record Addition Window\n' + '__________________')
        self.name_label = tkinter.Label(self.entry_frame, text='Enter Name:')
        self.name_entry = tkinter.Entry(self.entry_frame, width=30)

        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')
        
        self.id_label = tkinter.Label(self.id_frame, text='Enter Unique ID:')
        self.id_entry = tkinter.Entry(self.id_frame, width=20)

        self.id_label.pack(side='left')
        self.id_entry.pack(side='left')

        self.enter_button = tkinter.Button(self.enterbut_frame, text='Enter', command=self.enter)
        self.quit_button = tkinter.Button(self.enterbut_frame, text='Quit', command=self.add_window.destroy)

        self.enter_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.entry_frame.pack()
        self.id_frame.pack()
        self.enterbut_frame.pack() 
        self.n_frame.pack()

    def enter(self):
        st_id = int(self.id_entry.get())
        n =  str(self.name_entry.get())
        num = 0
        a = 0.0
        e = 'Not Eligible'


        # Insert a row of data
        c.execute("INSERT INTO students (student_id, name, number, attendance_percentage, eligibility) VALUES (?, ?, ?, ?, ?)",\
             (str(st_id), str(n), int(num), float(a), str(e)))
        conn.commit()
        tkinter.messagebox.showinfo('Response', 'Operation Successful!')

    def mark(self):
        self.mark_window = tkinter.Tk()

        self.msg_frame = tkinter.Frame(self.mark_window)
        self.class_frame = tkinter.Frame(self.mark_window)
        self.list_frame = tkinter.Frame(self.mark_window)
        self.bottom_frame = tkinter.Frame(self.mark_window)

        self.msg_label = tkinter.Label(self.msg_frame, text='Attendance Marking Window\n' +\
             '__________________\n' + 'Enter Student Id Number')
        self.msg_label.pack()

        self.class_label = tkinter.Label(self.class_frame, text='How many classes have been had? : ')
        self.class_entry = tkinter.Entry(self.class_frame, width=5)

        self.class_label.pack(side='left')
        self.class_entry.pack(side='left')

        self.submit_button = tkinter.Button(self.bottom_frame, text='Submit', command=self.submit)
        self.clear_button = tkinter.Button(self.bottom_frame, text='Clear', command=self.clear)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.mark_window.destroy)

        self.submit_button.pack(side='left')
        self.clear_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.list_label = tkinter.Label(self.list_frame, text='Enter your ID: ')
        self.list_entry = tkinter.Entry(self.list_frame, width=10)
        self.list_butt = tkinter.Button(self.list_frame, text='Enter', command=self.com)

        self.list_label.pack(side='left')
        self.list_entry.pack(side='left')
        self.list_butt.pack(side='left')
            

        self.msg_frame.pack()
        self.class_frame.pack()
        self.list_frame.pack()
        self.bottom_frame.pack()

    def com(self):
        i = int(self.list_entry.get())
        lists.append(i)
        tkinter.messagebox.showinfo('Response', 'Successful!')

    def submit(self):
        for item in lists:
            c.execute("SELECT number FROM students WHERE student_id = ?", (int(item),))
            d = c.fetchone()[0] + 1
            noc = int(self.class_entry.get())
            result = (d/noc) * 100
            c.execute("UPDATE students SET number =?, attendance_percentage =? WHERE student_id =?", (int(d), int(result), int(item),))
            conn.commit()
            if result >= 80:
                c.execute("UPDATE students SET eligibility = 'Eligible' WHERE student_id =?", (int(item),))
                conn.commit()
            else:
                c.execute("UPDATE students SET eligibility = 'Not eligible' WHERE student_id =?", (int(item),))
                conn.commit()
        for row in c.execute('SELECT student_id FROM students;'):
            if row not in lists:
                r = c.fetchone()[0]
                c.execute("SELECT number FROM students WHERE student_id = ?", (int(r),))
                a = c.fetchone()[0]
                noc = int(self.class_entry.get())
                result2 = (a/noc) * 100
                c.execute("UPDATE students SET attendance_percentage =? WHERE student_id =?", (int(result2), int(r),))
                conn.commit()
                if result2 >= 80:
                    c.execute("UPDATE students SET eligibility = 'Eligible' WHERE student_id =?", (int(r),))
                    conn.commit()
                else:
                    c.execute("UPDATE students SET eligibility = 'Not eligible' WHERE student_id =?", (int(r),))
                    conn.commit()

            
    def clear(self):
        lists.clear()

    def delete(self):
        self.delete_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.delete_window)
        self.input_frame = tkinter.Frame(self.delete_window)
        self.button_frame = tkinter.Frame(self.delete_window)

        self.top_label = tkinter.Label(self.top_frame, text='Record Deletion Window\n' + '________________')
        self.top_label.pack()

        self.input_label = tkinter.Label(self.input_frame, text='Enter ID of student record to delete: ')
        self.input_entry = tkinter.Entry(self.input_frame, width=10)

        self.input_label.pack(side='left')
        self.input_entry.pack(side='left')

        self.del_button = tkinter.Button(self.button_frame, text='Delete', command=self.delt)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.delete_window.destroy)

        self.del_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.input_frame.pack()
        self.button_frame.pack()
        
    def delt(self):
        d = int(self.input_entry.get())

        c.execute("DELETE FROM students WHERE student_id =?", (int(d), ))
        conn.commit()
        
        tkinter.messagebox.showinfo('Response', 'Delete Operation Successful!')
my_gui = My_GUI() 
