from bs4 import BeautifulSoup
import requests



r = open("New Player Missions.html")
content = r.read()

soup=BeautifulSoup(content,"html.parser")

result = []
flag = 0
import re
for i in soup.body.descendants:
    if i.name == "h1":
        if flag == 0:
            flag += 1
            result.append("> " + i.text.strip())
        elif flag == 1:
            flag += 1
            result.append("# " + i.text.strip())
    if flag != 2:
        continue
    else:
        try: print(i.prettify())
        except: pass
        if i.name == "h2":
            result.append("## " + i.text.strip())
        elif i.name == "h3":
            result.append("### " + i.text.strip())
        elif i.name == "h4":
            result.append("#### " + i.text.strip())
        elif i.name == "h5":
            result.append("##### " + i.text.strip())
        elif i.name == "table":
            print("table found",i.tbody.tr.th.text.strip())
            result.append(i.prettify())
        elif i.name == "p" or i.name == "a":
            result.append(re.sub('\s+', ' ', i.text.strip()))

    try: 
        if "href" in i.attrs:
            if i.attrs["href"].startswith("/wiki"):
                result[-1] = "[{}]({})".format(result[-1], i.attrs["href"].replace(":", "#"))
            else:
                result[-1] = "[{}]({})".format(result[-1], i.attrs["href"])

    except:
        continue

# print(""result)  
# print(len(result))
text = ("\n\n".join(result))

with open("test.md", "w") as f:
    f.write(text)
    