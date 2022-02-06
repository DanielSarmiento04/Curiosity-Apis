# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 12:41:24 2022

Nasa Api

@author: Daniel Sarmiento
"""


import requests
from datetime import datetime 
import os
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO

root = 'https://api.nasa.gov'

def FecthObservatory():
    urlConection = f"{root}/planetary/apod" #Url for link our project with nasa api
    dateToday = datetime.today()            #Complety Date 
    shortDayToday = dateToday.date()         #AAAA-MM-DD
    
    print(shortDayToday)
    
    #For get Apikey you have to request in https://api.nasa.gov/
    params = {                      # Keys
        'api_key' : os.environ['ApiKey'],                 
        'date': shortDayToday,  #You can choose a specify day 
        'hd' : True
        }

    response = requests.get(urlConection,params = params).json()#get response
    imagenUrl = str(response['url'])  #also, you can replace url with hdurl for improve resolution

    OpenUrl = requests.get(imagenUrl)  #Open url in a temporal file
    image = Image.open(BytesIO(OpenUrl.content)) #Open iamge file temporally
    plt.rcParams['figure.figsize'] = (9,9)  #put a specify weight and height
    plt.imshow(image)
    plt.title(shortDayToday)
    plt.axis('off')
    plt.show()
FecthObservatory()