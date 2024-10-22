#python tkinter tutorial
#tee-kinter , tk-inter , kinter

#starter code
# import tkinter
# from tkinter import * #method to import all things
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os                      #to check wheather the title is writte or not 
win= tk.Tk()     #instance variable is created for GUI   TK is constructor
win.title('GUI')        #for giving the title

#create labels
# widgets---labels,buttons, radio buttons--tk, ttk
name_label=ttk.Label(win,text="Enter your name : ")                 #pack() , grid()
name_label.grid(row=0, column=0,sticky=tk.W)                        #for stick in west

age_label=ttk.Label(win,text="Enter your age : ")
age_label.grid(row=1,column=0,sticky=tk.W)

email_label=ttk.Label(win,text="Enter your email id : ")
email_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text='Gender : ')
gender_label.grid(row=3,column=0,sticky=tk.W)

# create entry box
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()                #cursor position


age_var=tk.StringVar()                  #to save the data
age_entrybox=ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=1,column=1)

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=16,textvariable=email_var)
email_entrybox.grid(row=2,column=1)

# create combobox
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=13,textvariable=gender_var,state='readonly')
gender_combobox['values']=('Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

#radio button
usertype=tk.StringVar()
radiobutton1=ttk.Radiobutton(win,text='Student',value='Student',variable=usertype)
radiobutton1.grid(row=4,column=0)

radiobutton1=ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=usertype)
radiobutton1.grid(row=4,column=1)

#check button
checkbutn_var=tk.IntVar()
checkbutn=ttk.Checkbutton(win,text='if you want to subscribe newsletter',variable=checkbutn_var)
checkbutn.grid(row=5,columnspan=3)
#create button
# def action():
#     user_name = name_var.get()
#     user_age = age_var.get()
#     user_email = email_var.get()
#     print(f"your name is {user_name} and of {user_age} years and email is {user_email}")
#     user_gender = gender_var.get()
#     user_type = usertype.get()
#     user_check = checkbutn_var.get()
#     if checkbutn_var.get() == 0:
#         subscribed='NO'
#     else:
#         subscribed='YES'
#     print(f'{user_gender},{user_type},{user_check}')

#     with open('file.txt','a') as f:
#         f.write(f'{user_name},{user_age},{user_email},{user_gender},{user_type},{subscribed},\n')

#     name_entrybox.delete(0,tk.END)
#     age_entrybox.delete(0,tk.END)
#     email_entrybox.delete(0,tk.END)
#     name_label.configure(foreground='blue')      #google color picker
#     email_label.configure(foreground='#790e8b')
#     submit_button.configure(foreground='#c8b900')



def action():
    user_name = name_var.get()
    user_age = age_var.get()
    user_email = email_var.get()
    user_gender = gender_var.get()
    user_type = usertype.get()
    user_check = checkbutn_var.get()
    if checkbutn_var.get() == 0:
        subscribed='NO'
    else:
        subscribed='YES'
    with open('file1.csv','a',newline='') as f:
        dict_writer=DictWriter(f,fieldnames=["User Name",'User Email Address','User Age','User Gender','Type','Subscription'])
        if os.stat('file1.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'User Name': user_name,
            'User Email Address': user_email,
            'User Age': user_age,
            'User Gender': user_gender,
            'Type': user_type,
            'Subscription': subscribed})
    print(f"your name is {user_name} and of {user_age} years and email is {user_email},gender is {user_gender},Job is {user_type},subscription {subscribed}")
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    name_label.configure(foreground='blue')      #google color picker
    email_label.configure(foreground='#790e8b')
    submit_button.configure(foreground='#c8b900')



    
submit_button= tk.Button(win,text='Submit',command=action)
submit_button.grid(row=6,column=0)

win.mainloop()      #for creating a infinite loop so that we can show the window otherwise same instance it will close

