import requests
URL = "https://raw.githubusercontent.com/Daleindeed/cmput404-lab1/main/script.py"
r = requests.get(URL)
open('download.py', 'wb').write(r.content)