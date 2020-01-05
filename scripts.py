import subprocess
import webbrowser
import cgi
import sys
import hashlib
import pyfiglet

ascii_banner = pyfiglet.figlet_format("PySPORT")
print(ascii_banner)

index = open('index.html', "w")


print("Script Index.py Successeful [👍]")
subprocess.call("py sport.py")
subprocess.call("py divertissement.py")
subprocess.call("py cinema.py")
webbrowser.open_new("index.html")
index.close()     

print("Script Index.py Successeful [👍]")
index.close()



