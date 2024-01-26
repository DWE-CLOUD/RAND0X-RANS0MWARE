from bs4 import BeautifulSoup as bs
import os
import re
base = os.path.dirname(os.path.abspath(__file__))
html = open(os.path.join(base, '112.html'))
soup = bs(html, 'html.parser')
old_text = soup.find("div", {"id": "comp-l1ar3v9d"})
    b = "RANDOX ID : " + str(a)
    new_text = old_text.find(text=re.compile(
        'RANDOX ID : XXIOOPPAPAIJAOAJNKAK')).replace_with(b)
    xi = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(19))
    c = str(xi) + ".html"#earlier a
    from redmail import gmail
    gmail.username = 'randoxer@gmail.com'  # Your Gmail address
    gmail.password = 'pass_key'
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
    USERNAME = "epiz_32745950"
    PASSWORD = "2GoZAk2YIj"

    ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
    ftp_server.cwd('/htdocs')
    ftp_server.encoding = "utf-8"

    filename = str(xi) + ".html"
    with open(filename, "rb") as file:
        ftp_server.storbinary(f"STOR {filename}", file)

        ftp_server.quit()
    print("dwos.epizy.com/"+filename)