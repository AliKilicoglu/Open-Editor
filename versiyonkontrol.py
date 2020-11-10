from bs4 import BeautifulSoup
import requests
class Versiyon_Kontrol:
    def kontrol():
        dosya=open("versiyon.txt","r")
        dosya=dosya.read().replace("versiyon=","").replace("\n", "")

        istek = requests.get(url = "https://open-editor-versiyon-kontrol.tr.gg/")
        html = istek.text
        veri = BeautifulSoup(html, 'html.parser')
        a=veri.find('td',attrs={'class':'nav_heading'}).get_text()

        if a!=dosya:

            return "1"


        elif a==dosya:
            return "0"
