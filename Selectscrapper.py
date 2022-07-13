from Selectscrapper import request


def parse(txtpage):
    return

def createUrl(id):
    return "https://www.aladom.fr/" + id

def Cselect(id):
    url = createUrl(id)
    txtpage = request(url)
    if txtpage != 400:
        parse(txtpage)
    return