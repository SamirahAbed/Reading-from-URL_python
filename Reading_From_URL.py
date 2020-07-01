import requests
r = requests.get('https://en.wikipedia.org/wiki/COVID-19_pandemic')
print(r.text)

