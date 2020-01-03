import requests
import bs4
import webbrowser

index = open('index.html', "w")

link = ["http://channelstream.net/rmcsport_1.php", "http://channelstream.net/rmcsport_2.php",  "http://channelstream.net/rmcsport_3.php"]

rmc1 = "http://channelstream.net/rmcsport_1.php"
rmc2 = "http://channelstream.net/rmcsport_2.php"
rmc3 = "http://channelstream.net/rmcsport_3.php"

index.write("<div class='contener'>")
for url in link:
    chanel = requests.get(url)
    soup = bs4.BeautifulSoup(chanel.text, 'html.parser')
    frame_box = soup.find_all("iframe", {"id":"video"})
    text_box = soup.find_all("a", {"class":"article_titre"})
    index.write("<p>" + str(text_box) + "</p>")
    index.write(str(frame_box))
index.write("</div>")

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
print("Script Successeful [👍]")
index.close()






















































