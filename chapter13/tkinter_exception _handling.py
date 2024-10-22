import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
win=tk.Tk()
win.title('exeption handling')

#label frame
label_frame= ttk.LabelFrame(win, text='contact details')
label_frame.grid(row=0,column=0,padx=40,pady=10)

#labels
name_label=ttk.Label(label_frame,text="Enter your name : ", font=('Helvetica',14))
age_label=ttk.Label(label_frame,text='Enter your age : ',font=('Helvetica',14))

#entry box variables
name_var=tk.StringVar()
age_var=tk.StringVar()

#entry boxes
name_entry=ttk.Entry(label_frame,width=36,textvariable=name_var)
age_entry=ttk.Entry(label_frame,width=36,textvariable=age_var)

#grid
name_label.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
age_label.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)
name_entry.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
age_entry.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

# submit buton

def submit():
    # m_box.showinfo('title','content of this message box!!')
    # m_box.showerror('title','content of this message box!!')
    name=name_var.get()
    age=age_var.get()
    if name=="" or age=='':
        m_box.showwarning('Error','Plese fill details!!')
    else:
        try:
            age=int(age)
        except ValueError:
            m_box.showerror('Error','only digits are allowed in age fields')
        else:
            if age<18:
                m_box.showwarning('warning',"you are below 18")
            
            print(f"{name} : {age}")
submit_btn=ttk.Button(win,text='Submit',command=submit)
submit_btn.grid(row=1,columnspan=2,padx=40)
win.mainloop()

