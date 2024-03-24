import requests

payload = { 'api_key': '93e08b0ab2253158472121291a31849f', 'url': 'https://www.linkedin.com/in/aditigarg95/' } 
r = requests.get('https://api.scraperapi.com/', params=payload)
print(r.text)