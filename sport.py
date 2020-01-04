import requests
import bs4
import webbrowser

index = open('index.html', "w")

link = ["http://channelstream.net/rmcsport_1.php", "http://channelstream.net/rmcsport_2.php",  "http://channelstream.net/rmcsport_3.php", "http://channelstream.net/canal_sport-1.php", "http://channelstream.net/canal_sport_weekend.php", "http://channelstream.net/canal_premier_league.php", "http://channelstream.net/foot_plus.php"]

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

index.write("<div class='contener'>")
for url in link:
    chanel = requests.get(url)
    soup = bs4.BeautifulSoup(chanel.text, 'html.parser')
    frame_box = soup.find_all("iframe")
    text_box = soup.find_all("a", {"class":"article_titre"})
    index.write("<p>" + str(text_box) + "</p>")
    index.write(str(frame_box))
index.write("</div>")


print("Script Foot.py Successeful [👍]")
index.close()






















































