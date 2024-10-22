#for loop in tkinter
#previosly call tkinter contructor and work for all name,age , email one by one >>to create labels 
#padding>> to give the spacing between the rows.
import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('LOOP')
labels=['what is your name : ', 'what is your age : ',"what is your gender : ",'Country : ','State : ','City : ']



for i in range(len(labels)):
    cur_label='label' + str(i) # label0,label1
    cur_label=ttk.Label(win,text=labels[i])
    cur_label.grid(row=i, column=0, sticky=tk.W,padx=2,pady=2)
#entry box
user_info={
    'name':tk.StringVar(),
    'age':tk.StringVar(),
    'gender':tk.StringVar(),
    'country':tk.StringVar(),
    'state':tk.StringVar(),
    'city':tk.StringVar()
}
counter=0
for i in user_info:
    cur_entrybox='entry'+i
    cur_entrybox=ttk.Entry(win,width=16,textvariable=user_info[i])
    cur_entrybox.grid(column=1,row=counter,padx=2,pady=2)
    counter+=1
def submit():
    print(user_info['name'].get())
    print(user_info['age'].get())
    print(user_info['gender'].get())
    print(user_info['country'].get())
    print(user_info['state'].get())
    print(user_info['city'].get())

submit_btn=ttk.Button(win,text='Submit',command=submit)
submit_btn.grid(row=6,columnspan=2)

# name_var=tk.StringVar()
# name_entry=ttk.Entry(win,width=16,textvariable=name_var)
# name_entry.grid(row=0,column=1)


win.mainloop()