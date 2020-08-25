from bs4 import BeautifulSoup
import requests
f = open("abc.txt","a")
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
control =False
for z in range(3000000,4000000):
    x = requests.get("https://brainly.in/question/"+str(z)+"",headers=headers)
    page=x.content.decode("UTF-8")
    soup = BeautifulSoup(page,"html.parser")
    tag = soup.findAll('li', {"class": "sg-breadcrumb-list__element"})
    for i in tag:
        if i.get_text().strip() == "Math":
            control = True

    if control == True:
        question = soup.findAll("div", {"class": "brn-content-image"})
        answer = soup.findAll("div", {"class": "brn-answer__text"})
# if question is None or answer is None:
    # pass
# else:

        for i in question:
            f.write("Q) "+i.get_text().strip()+"\n")

        for i in answer:
            f.write("Answer "+i.get_text().strip()+"\n")
            f.write("\n")

        f.write("----------------------------------------------------------------------------------------------------------------")
        f.write("\n")
        control = False
    else:
        pass
    print(z)

