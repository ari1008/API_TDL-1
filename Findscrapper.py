from posixpath import split
import re
import requests


#decoup la page avec que ce qui nous interesse 
def parse(content_url):
    list_content_url = list(content_url.split('\n'))
    index = list_content_url.index('    <div class="row offer-list">')
    list_content_url = list_content_url[index:]
    index2 = list_content_url.index('      <div class="row">')
    list_content_url = list_content_url[:index2+1]
    ListRes = findElement(list_content_url)
    return ListRes

#recupère url de l'image dans la balise <img>
def recupUrlIMG(imgStr):
    list_img = list(imgStr.split(" "))
    for element in list_img:
        if "data-src=" in element:
            return element[element.find("\""):element.rfind("\"")]

#recherche information dans élement 
def findInfoIntoElement(listElement):
    dictInfo = {}
    for i in range(0, len(listElement)):
        if listElement[i] == "    <figure>":
            dictInfo["URL_INFO"] = recupUrlIMG(listElement[i+1])
    return dictInfo

#recherce element
def findElement(listElement):
    ListRes = []
    first = ""
    for i in range(0, len(listElement)):
        if listElement[i] == '        <div class="col-lg-4 col-6 d-flex flex-column my-4 offer-list-item">':
            if first == "":
                first = i
            else:
                ListRes.append(findInfoIntoElement(listElement[first:i]))
                first = i
    print(ListRes)
    return ListRes

#prend en paramètre l'url de la page 
def request(url):
    r = requests.get(url)
    if (r.status_code != 200):
        print("erreur")
        return r.status_code
    else:
        parse(r.content.decode("utf-8"))


request("https://www.aladom.fr/aide-personnes-handicapees/paris-75/")


