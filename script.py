import requests
URL = "https://raw.githubusercontent.com/Daleindeed/cmput404-lab1/main/script.py"
r = requests.get(URL)
# writing to a file with the content
# discarded upon clarification from Abram
# open('download.py', 'wb').write(r.content)
print(r.content)
