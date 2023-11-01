#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import os

save_dir="images/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

query="Elon Musk"#You can you use any name for the images
response=requests.get(f"https://www.google.com/search?q={query}&sca_esv=578489342&hl=en&tbm=isch&sxsrf=AM9HkKlf_HX6JnrHeBDrFu7TZvpf_Fx9Gg%3A1698847007087&source=hp&biw=1370&bih=641&ei=H1lCZZTJAufhxc8PyrupkAM&iflsig=AO6bgOgAAAAAZUJnL_JKTDYGzyfDI94RsFkFP-3yo7zj&oq=sudh&gs_lp=EgNpbWciBHN1ZGgqAggAMgQQIxgnMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESKwZULsEWLUMcAF4AJABAJgBmQKgAZUIqgEDMi00uAEByAEA-AEBigILZ3dzLXdpei1pbWeoAgrCAgcQIxjqAhgnwgIIEAAYgAQYsQPCAgsQABiABBixAxiDAQ&sclient=img")
print(response)

soup=BeautifulSoup(response.content,"html.parser")
images_tag=soup.find_all("img")
print(len(images_tag))
del images_tag[0]
print(images_tag)
for i in images_tag:
    images_url=i["src"]
    image_data=requests.get(images_url).content
    with open(os.path.join(save_dir,f"{query}_{images_tag.index(i)}.jpg"),"wb") as f:
        f.write(image_data)

