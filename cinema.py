import requests
import bs4
import webbrowser

index = open('cinema.html', "w")

index.write("<!DOCTYPE html>"
+ "<html lang='en'>"
+ "<head>" +
    "<meta charset='UTF-8'>"+
    "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"+
    "<meta http-equiv='X-UA-Compatible' content='ie=edge'>" +
    "<link href='style.css' rel='stylesheet'>" +
    "<title>PySPORT</title>"+
"</head>"+
"<body>"+

"</body>"+
"</html>")

index.write("<div class='navbar'>")
index.write("<a href='index.html' class='ongletmain'>Sport</a>")
index.write("<a href='divertissement.html' class='onglet'>Divertissement</a>")
index.write("<a href='cinema.html' class='onglet'>Cinema</a>")
index.write("</div>")

link = ["http://123sport.tv/canal.php", "http://123sport.tv/canal-cinema.php", "http://123sport.tv/canal-decale.php"]

index.write("<div class='contener'>")
for url in link:
    chanel = requests.get(url)
    soup = bs4.BeautifulSoup(chanel.text, 'html.parser')
    frame_box = soup.find_all("iframe")
    text_box = soup.find_all("div", {"class":"details col-sm-6"})
    index.write(str(text_box))
    index.write("<div class='boxmain'>")
    index.write("<div class='box'>")
    index.write(str(frame_box))
    index.write("</div>")
    index.write("</div>")
index.write("</div>")

print("Script Cinema.py Successeful [👍]")
index.close()