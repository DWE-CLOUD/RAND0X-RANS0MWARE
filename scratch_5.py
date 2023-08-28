from tkinter import *
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
# GUI
import string
import random

# initializing size of string
N = 12

# using random.choices()
# generating random strings
res = ''.join(random.choices(string.ascii_uppercase +
							string.digits, k=N))
print(str(res))
# print result

import ftplib
import time

FTP_HOST_1 = "ftpupload.net"
FTP_USER_1 = "epiz_32745950"
FTP_PASS_1 = "2GoZAk2YIj"
ftp_1 = ftplib.FTP(FTP_HOST_1, FTP_USER_1, FTP_PASS_1)
ftp_1.encoding = "utf-8"
ftp_1.cwd("./htdocs")
input_db=str(res)
ftp_new_dir = ftp_1.mkd(input_db)
ftp_1.cwd(input_db)
ftp_new_dir1 = ftp_1.mkd("Attacked")
ftp_new_dir2 = ftp_1.mkd("Attacker")
#ftp_1.dir()

root = Tk()
root.title("Connected to Network . IP : "+str(IPAddr))

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
n12=[]
def upload(filename):
    with open(filename, "rb") as file:
        # Command for Uploading the file "STOR filename"
        ftp_1.storbinary(f"STOR {filename}", file)
def sending(sendme):
    if len(n12)==0:
        ftp_1.cwd("Attacker")
    n12.append("1")
    from Crypto.Random import get_random_bytes
    from Crypto.Cipher import AES, PKCS1_OAEP
    from Crypto.PublicKey import RSA

    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out = open("private.pem", "wb")
    file_out.write(private_key)
    file_out.close()

    public_key = key.publickey().export_key()
    file_out = open("receiver.pem", "wb")
    file_out.write(public_key)
    file_out.close()
    data = sendme.encode("utf-8")
    file_out = open("encrypted_data.bin", "wb")

    recipient_key = RSA.import_key(open("receiver.pem").read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    file_out.close()
    # Enter File Name with Extension
    # Read file in binary mode
    upload("encrypted_data.bin")
    upload("private.pem")
    upload("receiver.pem")
def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)

    user = e.get().lower()

    if user:
        sending(user)
        txt.insert(END, "\n" + "Message Sent !")

    e.delete(0, END)
def receiver():
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import AES, PKCS1_OAEP

    file_in = open("encrypted_data.bin", "rb")

    private_key = RSA.import_key(open("private.pem").read())

    enc_session_key, nonce, tag, ciphertext = \
       [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

    # Decrypt the session key with the private RSA key
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    # Decrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    txt.insert(END, "\n" + "DWE ( ADMIN ) -> "+str(data.decode("utf-8")))
def refresh():
    ftp_1.cwd("Attacked")
    for i in range(5):
        fileSize = ftp_1.size("encrypted_data.bin")
        if fileSize < 0:
            print("not found")
        else:
            print("found")
            filename = "encrypted_data.bin"
            with open(filename, "wb") as file:
                # Command for Downloading the file "RETR filename"
                ftp_1.retrbinary(f"RETR {filename}", file.write)
                file.close()
                receiver()
                n12.clear()
                break

lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Rand0X ID : "+str(res), font=FONT_BOLD, pady=10, width=20, height=1).grid(
    row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
            command=send).grid(row=2, column=1)
refresh = Button(root, text="Refresh", font=FONT_BOLD, bg=BG_GRAY,
            command=refresh).grid(row=3, column=1)
root.mainloop()
