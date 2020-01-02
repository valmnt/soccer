import requests
import bs4
import webbrowser

index = open('index.html', "w")

rmc1 = "http://channelstream.net/rmcsport_1.php"
rmc2 = "http://channelstream.net/rmcsport_2.php"
rmc3 = "http://channelstream.net/rmcsport_3.php"

r1 = requests.get(rmc1)
r2 = requests.get(rmc2)
r3 = requests.get(rmc3)

soup1 =  bs4.BeautifulSoup(r1.text, 'html.parser')
soup2 =  bs4.BeautifulSoup(r2.text, 'html.parser')
soup3 =  bs4.BeautifulSoup(r3.text, 'html.parser')

frame_box1 = soup1.find_all("iframe", {"id":"video"})
frame_box2 = soup2.find_all("iframe", {"id":"video"})
frame_box3 = soup3.find_all("iframe", {"id":"video"})

text_box1 = soup1.find_all("a", {"class":"article_titre"})
text_box2 = soup2.find_all("a", {"class":"article_titre"})
text_box3 = soup3.find_all("a", {"class":"article_titre"})

index.write("<!DOCTYPE html>"
+ "<html lang='en'>"
+ "<head>" +
    "<meta charset='UTF-8'>"+
    "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"+
    "<meta http-equiv='X-UA-Compatible' content='ie=edge'>" +
    "<link href='style.css' rel='stylesheet'>" +
    "<title>Document</title>"+
"</head>"+
"<body>"+

"</body>"+
"</html>")

index.write("<div class='contener'>")
index.write("<p>"+ str(text_box1) + "</p>")
index.write(str(frame_box1))
index.write("<p>"+ str(text_box2) + "</p>")
index.write(str(frame_box2))
index.write("<p>"+ str(text_box3) + "</p>")
index.write(str(frame_box3))
index.write("</div>")
index.close()























































