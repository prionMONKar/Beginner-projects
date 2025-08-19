import http.server                                                    #for implementing the http web servers
import socket                                                         #provides access to the BSD socket interface
import socketserver                                                   #a framework for network servers
import webbrowser                                                     #to display a web based documents to users
import png                                                            #convert into png format
import os                                                             #to access operating system control
import pyqrcode                                                       #to generate qrcode
from pyqrcode import QRCode

PORT = 8010                                                           #assigning the appropriate port value

os.environ['USERPROFILE']                                             #this finds the name of the computer user
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),       #changing the directory to access the files desktop with the help of os module
                       'OneDrive')
os.chdir(desktop)

Handler = http.server.SimpleHTTPRequestHandler                        #creating a http request

hostname = socket.gethostname()                                       #returns the host name of the system under which Python interpreter is executed

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                  #finding the IP address of the PC
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP

url = pyqrcode.create(link)                                           #converts the IP address into a Qrcode
url.svg("myqr.svg", scale = 8)                                        #saves the Qrcode inform of svg

webbrowser.open('myqr.svg')                                           #opens the Qrcode image in the web browser

with socketserver.TCPServer(("",PORT), Handler) as httpd:             #continuous stream of data between client and server
    print("Serving at port", PORT)
    print("Type this in your Browser", IP)
    print("or Use the QRCode")
    httpd.serve_forever()