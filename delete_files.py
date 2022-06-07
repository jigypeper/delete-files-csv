import csv
import os
import time
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import *
y =[]
file_csv = ''
dir = ''

def run_help():
    helproot = tk.Tk()
    helproot.iconbitmap("C:/Users/ahmed/pythontut/program/df.ico")
    help_text = tk.Text(helproot, height=20, width=100)
    helproot.title('Instructions')
    help_text.pack()
    help_text.insert(tk.END, "1. List files you want to delete (without extension) in excel\n2. Save as a CSV file\n3. Select the CSV you created, with 'Open CSV File' button\n4. Select the folder you want to delete from, with 'Set Directory' button\n5. Delete files, with 'Delete Files' button\n")
    helproot.mainloop()


root = tk.Tk()
root.iconbitmap("C:/Users/ahmed/pythontut/program/df.ico")
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label='Help', menu=subMenu)
subMenu.add_command(label='How to use', command= run_help)

root.title('Delete Multiple Files')
root.geometry('400x160')

def open_file():
    global file_csv
    root.filename = filedialog.askopenfilename(filetypes=(("CSV Files","*.csv"),))
    file_csv = root.filename
    c = "Selected file: " + file_csv
    label2['text'] = c
    

def set_dir():
    global dir
    dir = filedialog.askdirectory()
    c = "Selected Directory: " + dir
    label3['text'] = c

def work_csv():
    global y
    files = csv.reader(open(file_csv))
    y = []
    for line in files:
        x = line.pop()
        y.append(x)

def delete_files():
    work_csv()
    for i in y:
        c = "Scanning for " + i
        root.update_idletasks()
        time.sleep(0.1)
        label1['text'] = c
        for fname in os.listdir(dir):
            f = os.path.join(dir,fname)
            if fname.startswith(i):
                if (os.path.exists(f)):
                    c = "Deleting " + f
                    root.update_idletasks()
                    time.sleep(0.1)
                    label1['text'] = c
                    os.chmod(f, 0o777)
                    try:
                        os.remove(f)
                    except OSError:
                        try:
                            shutil.rmtree(f)
                        except:
                            c = "Need permissions to remove " + f
                            label1['text'] = c
                else:
                    c = "Skipping "+f+"not prefixed with" + i
                    root.update_idletasks()
                    time.sleep(0.1)
                    label1['text'] = c
    c = 'Finished, update selections to run again'
    label1['text'] = c

button1 = tk.Button(root, text= 'Open CSV File', width= 400, command= open_file)
button2 = tk.Button(root, text= 'Set Directory', width= 400, command= set_dir)
button3 = tk.Button(root, text= 'Delete Files', width= 400, command= delete_files)
button1.pack()
button2.pack()
button3.pack()
label1 = tk.Label(root, text= file_csv, bd=1, relief=SUNKEN, anchor=W)
#label1 = tk.Label(root, text= file_csv, bg="black", fg="white", width=400)
label2 = tk.Label(root, text= file_csv, bg="black", fg="white", width=400)
label3 = tk.Label(root, text= dir, bg="black", fg="white", width=400)
label2.pack()
label3.pack()
label1.pack(side=BOTTOM, fill=X)
root.mainloop()