# Tokyo in WiFi
アイドルグループ・・・・・・・・・第15回定期公演「Tokyo in WiFi」特設Webサイト(Single Page Application)

[https://wifi.dots.tokyo](https://wifi.dots.tokyo)

## Description
本サイトをスマホで開きながら世界各地に設置されたスポットを訪れると、アイドルの音声や動画を閲覧することができます。  
音声や動画のなかには、そのスポットが設置された場所にちなんだ内容のものもあり、あたかもアイドルがそこに棲んでいるような錯覚を生みだします。  

## Requirement
- Django 2.1.5  
- Python 3.6.1
- HTML5 Geolocation API
- jQuery 3.3.1
- Heroku
- PostgreSQL

## Screenshot
<img src="http://d3jo9wp4rp1004.cloudfront.net/technology/tokyo_in_wifi/connect_wifi_poster.png" width="400" height="711">

## Demo
[http://d3jo9wp4rp1004.cloudfront.net/technology/tokyo_in_wifi/connect_wifi.mov](http://d3jo9wp4rp1004.cloudfront.net/technology/tokyo_in_wifi/connect_wifi.mov)

## Usage
```
$ git clone git@github.com:a-r-i/tokyo_in_wifi_website.git
$ cd tokyo_in_wifi_website
$ pip install -r requirements.txt
```

make settings_local.py.

```
SECRET_KEY = ''
DEBUG = True
ALLOWED_HOSTS = [
                'localhost/',
                'localhost',
                '127.0.0.1/',
                '127.0.0.1',
                ]
SECURE_SSL_REDIRECT = False
```

open settings.py.  
uncomment settings_local, and commentout settings_production.

```
from settings_local import SECRET_KEY, DEBUG, ALLOWED_HOSTS, SECURE_SSL_REDIRECT
# from settings_production import SECRET_KEY, DEBUG, ALLOWED_HOSTS, SECURE_SSL_REDIRECT
```

```
$ python manage.py migrate
$ python manage.py runsslserver
```

access to https://127.0.0.1:8000/spots.