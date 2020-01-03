import requests
import bs4
import webbrowser

index = open('divertissement.html', "w")

index.write("<!DOCTYPE html>"
+ "<html lang='en'>"
+ "<head>" +
    "<meta charset='UTF-8'>"+
    "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"+
    "<meta http-equiv='X-UA-Compatible' content='ie=edge'>" +
    "<link href='style.css' rel='stylesheet'>" +
    "<title>FCMONt</title>"+
"</head>"+
"<body>"+

"</body>"+
"</html>")

index.write("<div class='navbar'>")
index.write("<a href='index.html' class='ongletmain'>Sport</a>")
index.write("<a href='divertissement.html' class='onglet'>Divertissement</a>")
index.write("<a href='cinema.html' class='onglet'>Cinema</a>")
index.write("</div>")

link = ["http://channelstream.net/national-geo.php", "http://channelstream.net/national-geo-wild.php", "http://channelstream.net/voyage.php", "http://channelstream.net/planete.php"]

index.write("<div class='contener'>")
for url in link:
    chanel = requests.get(url)
    soup = bs4.BeautifulSoup(chanel.text, 'html.parser')
    frame_box = soup.find_all("iframe")
    text_box = soup.find_all("a", {"class":"article_titre"})
    index.write("<p>" + str(text_box) + "</p>")
    index.write(str(frame_box))
index.write("</div>")

print("Script Divertissement.py Successeful [👍]")
index.close()