# Utilisation

`python slideshare_parser.py --url=url_du_diaporama_slideshare_a_recuperer`

# Le principe

1. Récupérer l'URL du diaporama souhaité

	Exemple : `https://fr.slideshare.net/ctin/windows-7-forensics-overviewr3`

2. Dans la source de la page, on récupére l'URL (href) du JSON décrivant la structure des diapositives. Le titre du lien est "Slideshow json oEmbed Profile".
    Exemple : `<link title="Slideshow json oEmbed Profile" type="application/json+oembed" href="https://fr.slideshare.net/api/oembed/2?format=json&amp;url=http://www.slideshare.net/ctin/windows-7-forensics-overviewr3" rel="alternate">`

3. On peut ensuite récupérer le JSON : 
    Exemple de contenu :
```
{
    "version":"1.0",
    "type":"rich",
    "title":"Windows 7 forensics -overview-r3",
    "author_name":"CTIN",
    "author_url":"https://www.slideshare.net/ctin",
    "provider_name":"SlideShare",
    "provider_url":"https://fr.slideshare.net/",
    "html":"\u003Ciframe src=\"https://www.slideshare.net/slideshow/embed_code/key/6rhrqyHgcfjGdx\" width=\"427\" height=\"356\" frameborder=\"0\" marginwidth=\"0\" marginheight=\"0\" scrolling=\"no\" style=\"border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;\" allowfullscreen\u003E \u003C/iframe\u003E \u003Cdiv style=\"margin-bottom:5px\"\u003E \u003Cstrong\u003E \u003Ca href=\"https://www.slideshare.net/ctin/windows-7-forensics-overviewr3\" title=\"Windows 7 forensics -overview-r3\" target=\"_blank\"\u003EWindows 7 forensics -overview-r3\u003C/a\u003E \u003C/strong\u003E de \u003Cstrong\u003E\u003Ca href=\"https://www.slideshare.net/ctin\" target=\"_blank\"\u003ECTIN\u003C/a\u003E\u003C/strong\u003E \u003C/div\u003E\n\n",
    "width":425,
    "height":355,
    "thumbnail":"//cdn.slidesharecdn.com/ss_thumbnails/windows7forensics-overview-r3-110606165431-phpapp02-thumbnail.jpg?cb=1422657743",
    "thumbnail_url":"https://cdn.slidesharecdn.com/ss_thumbnails/windows7forensics-overview-r3-110606165431-phpapp02-thumbnail.jpg?cb=1422657743",
    "thumbnail_width":170,
    "thumbnail_height":128,
    "total_slides":98,
    "conversion_version":2,
    "slide_image_baseurl":"//image.slidesharecdn.com/windows7forensics-overview-r3-110606165431-phpapp02/95/slide-",
    "slide_image_baseurl_suffix":"-1024.jpg",
    "version_no":"1422657743",
    "slideshow_id":8227368
}
```

4. Dans le JSON on récupère les informations suivantes :
  - `slide_image_baseurl` : l'URL de base des diapo
  - `slide_image_baseurl_suffix` : le suffixe de l'URL qui donne la dimension et le format des diapos
  - `total_slides` : le nombre total de diapositives

 5. Il est maintenant possible de récupérer les slides (au format JPEG) en construisant les URLs de la manière suivante :
   - https:`slide_image_baseurl` `slide_number` `slide_image_baseurl_suffix`
   - Exemple d'URL : `https://image.slidesharecdn.com/windows7forensics-overview-r3-110606165431-phpapp02/95/slide-1-1024.jpg`
   
   
-------
   
# Automatisation
Il est possible de tout automatiser comme cela est fait dans le script suivant : 
- [slideshare_parser.py](slideshare_parser.py)

# Dépendances
Le script a les dépendances suivantes :
- Python 2.7
- bibliothèques python :
	- PIL (pip install Pillow)
	- reportlab (https://bitbucket.org/rptlab/reportlab)
	- BeautifulSoup 4 (pip install bs4)
	- requests (pip install requests)
