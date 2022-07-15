from ensurepip import version
from Findscrapper import request

# récupère le titre de la page d'apres la balise title 
def recoveryTitle(title):
    return title[5:title.find('</title>')]

def recoveryDesc(tab , index):
    desc = (tab[index])[tab[index].find('content='):]
    while True:
        index = index + 1
        if '">' in tab[index]:
            break
        desc = desc + " " +  tab[index]
    desc = desc + " " +  (tab[index])[:len(tab[index])-2]
    return desc

def recoveryTitleAndDesc(tab):
    dictres = {}
    index = tab.index('  <!-- End Adsense -->')
    i = index
    while True:
        if index+100 == i:
            print("ERROR")
            break
        if '<title>' in tab[i]:
            dictres["TITLE"] = recoveryTitle(tab[i])
        if '<meta name="description"' in tab[i]:
            dictres["DESC"] = recoveryDesc(tab, i)
            break
        i = i + 1
    return dictres

# tri si la page est en version pro ou pas ! 
def parse(txtpage):
    list_content_url = list(txtpage.split('\n'))
    dictres = recoveryTitleAndDesc(list_content_url)
    try:
        index = list_content_url.index('          <div class="offer-service-card ">')
        dictres = NOPro(dictres, list_content_url[index:])
    except ValueError:
        dictres = pro(dictres)
    return dictres 

def recoveryPriceNet(priceLine):
    return priceLine[priceLine.find('">')+2:priceLine.find('</div>')]

def recoveryPrice(priceLine):
    return priceLine[priceLine.find("t")+1:priceLine.find("a")]

def NOPro(dictres, list_content):
    index = list_content.index('        <div class="offer-content col-md-7 order-md-1">')
    for i in range(0, index):
        if "price-info mt-3" in list_content[i]:
            dictres["NET_PRICE"] = recoveryPriceNet(list_content[i])
        if "price-info-cesu" in list_content[i]:
            dictres["PRICE"] = recoveryPrice(list_content[i+2])
    return dictres

def pro(dictres):
    return dictres

#crée l'url avec l'id rentré dans la page
def createUrl(id):
    return "https://www.aladom.fr/" + id

def Cselect(id):
    url = createUrl(id)
    txtpage = request(url)
    print(url)
    if txtpage != 400:
        print(parse(txtpage))
    return

Cselect("aide-personnes-handicapees/paris_15eme-75/carlos-28-ans-aide-aux-personnes-handicapees-516u")
Cselect("aide-personnes-handicapees/paris_13eme-75/aide-a-domicile-pour-les-personnes-en-situation-de-dependance-etou-handicap-74st")