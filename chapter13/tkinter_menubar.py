import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title("menubar tutorial")
def func():
    print('func called')
# **********************simple menubar***********************
#Menu
# menubar=tk.Menu(win)
# menubar.add_command(label='Save', command=func)
# menubar.add_command(label='Save As', command=func)
# menubar.add_command(label='Copy', command=func)
# menubar.add_command(label='Paste', command=func)
main_menu= tk.Menu(win)
file_menu=tk.Menu(main_menu,tearoff=0)

file_menu.add_command(label='New file', command=func)
file_menu.add_command(label='New Window', command=func)
#seprator function
file_menu.add_separator()

file_menu.add_command(label='Save file', command=func)


#edit menu
edit_menu= tk.Menu(main_menu,tearoff=0)
edit_menu.add_command(label='Undo',command=func)
edit_menu.add_command(label='Redo',command=func)
edit_menu.add_command(label='Cut',command=func)
main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='Edit',menu=edit_menu)


win.config(menu=main_menu)



win.mainloop()