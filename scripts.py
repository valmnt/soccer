import subprocess
import webbrowser
import cgi
import sys
import hashlib
import pyfiglet

ascii_banner = pyfiglet.figlet_format("PySPORT")
print(ascii_banner)

index = open('index.html', "w")

code = "5c3dba7f46545a7b608fd7ef8954c2cb"
compteur = 0

form = cgi.FieldStorage()
keycodes = form.getvalue('keycode')
keycodes = input("Entrez la clé d'abonnement: ")

if(keycodes == code):
    print("Script Index.py Successeful [👍]")
    subprocess.call("py sport.py")
    subprocess.call("py divertissement.py")
    subprocess.call("py cinema.py")
    webbrowser.open_new("index.html")
    index.close()     
else:
    print("ERF....")
    sys.exit()

print("Script Index.py Successeful [👍]")
index.close()



