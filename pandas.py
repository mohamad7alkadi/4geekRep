#!/usr/bin/env python
# coding: utf-8

# In[141]:


import pandas as pd


# In[ ]:





# In[147]:


from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import pandas as pd
import time


# In[28]:


path={'chromedriver'}


# In[29]:


chrome_options = Options()


# In[30]:





# In[229]:


myExcelFrame = pd.read_excel ('/Users/MAC/Desktop/git4geeks/4geekRep/Klinikliste.xlsx' )


# In[230]:


columns


# In[231]:


myExcelFrame.index


# In[235]:


myExcelFrame


# In[237]:


myExcelFrame['Klinikname']


# In[243]:


myExcelFrame['Klinikname'][0]


# In[244]:


myExcelFrame['Link Google Maps'][0]


# In[250]:


myExcelFrame['Link Klinikbewertungen'][0]


# In[245]:


#Now Can We Use requests


# In[248]:


#Sample Code to Use R and BeautifulSoup


# In[249]:


from bs4 import BeautifulSoup
import requests


# In[251]:


link0 = myExcelFrame['Link Klinikbewertungen'][0]


# In[252]:


link0


# In[254]:


page = requests.get(link0)


# In[256]:


page #Important <Response [200]> is Ok.


# In[257]:


#Now Use BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')


# In[258]:


#Get Title From Web Scraping
title = soup.find(itemprop="name")


# In[259]:


print(title)


# In[260]:


title.text


# In[261]:


title.text


# In[ ]:




