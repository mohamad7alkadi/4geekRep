# 4geekRep
#Folgenden Werden Benötigt
    from selenium import webdriver 
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver import Chrome
    import pandas as pd
    import time
    
    
    
    #Get Data Using request and BeautifulSoup 
    from bs4 import BeautifulSoup
    import requests
        #BeiSpiel Link1 = 'https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-lindenbrunn-coppenbruegge'
        page = requests.get(link1)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(itemprop="name")
        print(title)
        #<h1 itemprop="name" style="display:inline-block">Krankenhaus Lindenbrunn</h1>

path={'chromedriver'}  #Download Chrome Driver From URL: Please Visit This URL https://chromedriver.chromium.org/ then Download Driver and Past in Your Path in Project Directory
chrome_options = Options()
#Dataframe using Pandas
df = pd.read_excel ('/Users/MAC/Desktop/git4geeks/4geekRep/Klinikliste.xlsx' )
df.index # Rows Counter   //#RangeIndex(start=0, stop=24, step=1)
columns   # Index(['Klinikname;Link Google Maps;Link Klinikbewertungen'], dtype='object')

