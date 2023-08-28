from bs4 import BeautifulSoup as bs
import os
import re

# Remove the last segment of the path
base = os.path.dirname(os.path.abspath(__file__))

# Open the HTML in which you want to make changes
html = open(os.path.join(base, '112.html'))

# Parsing in Beautiful Soup
soup = bs(html, 'html.parser')
old_text = soup.find("div", {"id": "comp-l1ar3v9d"})
    b = "RANDOX ID : " + str(a)
    # Replace the already stored text with
    # the new text which you wish to assign
    new_text = old_text.find(text=re.compile(
        'RANDOX ID : XXIOOPPAPAIJAOAJNKAK')).replace_with(b)
    xi = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(19))
    c = str(xi) + ".html"#earlier a
    from redmail import gmail
    gmail.username = 'dwepay.india@gmail.com'  # Your Gmail address
    gmail.password = 'pllbckjjqnnifktz'
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

    # Fill Required Information
    HOSTNAME = "ftpupload.net"
    USERNAME = "epiz_32745950"
    PASSWORD = "2GoZAk2YIj"

    # Connect FTP Server
    ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
    ftp_server.cwd('/htdocs')
    ftp_server.encoding = "utf-8"
    # Enter File Name with Extension
    filename = str(xi) + ".html"
    # Read file in binary mode
    with open(filename, "rb") as file:
        ftp_server.storbinary(f"STOR {filename}", file)
        # Get list of files
        # Close the Connection
        ftp_server.quit()
    print("dwos.epizy.com/"+filename)