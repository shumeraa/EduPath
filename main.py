import requests

response = requests.get('https://one.ufl.edu/apix/soc/schedule/?category=CWSP&term=2235')
print(response.text)