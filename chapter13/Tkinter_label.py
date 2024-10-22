import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('Label Frame')

label_frame= ttk.LabelFrame(win,text='Enter your details below')
label_frame.grid(row=0, column=0,padx=40)
labels=['what is your name : ', 'what is your age : ',"what is your gender : ",'Country : ','State : ','City : ']



for i in range(len(labels)):
    cur_label='label' + str(i) # label0,label1
    cur_label=ttk.Label(label_frame,text=labels[i])
    cur_label.grid(row=i, column=0, sticky=tk.W)

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
    cur_entrybox=ttk.Entry(label_frame,width=16,textvariable=user_info[i])
    cur_entrybox.grid(column=1,row=counter)
    counter+=1
def submit():
    print(user_info['name'].get())
    print(user_info['age'].get())
    print(user_info['gender'].get())
    print(user_info['country'].get())
    print(user_info['state'].get())
    print(user_info['city'].get())

submit_btn=ttk.Button(win,text='Submit',command=submit)
submit_btn.grid(row=1,column=0)

for child in label_frame.winfo_children():        #to give the padding between in
    child.grid_configure(padx=4,pady=4)



win.mainloop()