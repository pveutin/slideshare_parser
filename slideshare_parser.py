#!/usr/bin/python
# coding: utf-8
__author__ = "Rooxy"
__copyright__ = "Copyright 2018, Rooxy"
__license__ = "GPL v3"
__version__ = "1.0"
__maintainer__ = "Rooxy"
__email__ = "veutinpierre@gmail.com"
__status__ = "Production"

import requests
import json
import urllib
import os
import argparse

from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import Image

parser = argparse.ArgumentParser(description='Récupère les dispos de slideshare')
parser.add_argument('-u', '--url', help='url du diaporama a récupérer', required=True, dest="url")
results = parser.parse_args()
url = results.url
resultat = requests.get(url)
page = resultat.content
soup = BeautifulSoup(page,  "html.parser")
link = soup.find('link', {"title":"Slideshow json oEmbed Profile"})
url_json = link['href']
structure = requests.get(url_json)
j = json.loads(structure.content) 
base_url = "https:"+j['slide_image_baseurl']
slide_count = j['total_slides']

try: 
    os.makedirs(j['title'])
except OSError:
    if not os.path.isdir(j['title']):
        raise
c = canvas.Canvas(j['title']+'.pdf')
c.setPageSize( landscape(letter) )
width,height = landscape(letter)

for i in range(slide_count):
	uri = base_url+str(i+1)+j['slide_image_baseurl_suffix']
	urllib.urlretrieve (uri, './'+j['title']+'/'+str(i+1)+j['slide_image_baseurl_suffix'])
	c.drawImage('./'+j['title']+'/'+str(i+1)+j['slide_image_baseurl_suffix'], 1*inch, 1*inch, width-2*inch, height-2*inch)
	c.showPage()
c.save()
