import requests

# URL de la API de CoinMarketCap
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# Parámetros de la solicitud HTTP
params = {'symbol': 'BTC,ETH', 'convert': 'USD'}

# Encabezados de la solicitud HTTP (reemplaza 'API_KEY' con tu clave de API de CoinMarketCap)
headers = {'X-CMC_PRO_API_KEY': 'API_KEY'}

# Realiza una solicitud HTTP GET a la API de CoinMarketCap
response = requests.get(url, params=params, headers=headers)

# Analiza la respuesta JSON
data = response.json()

# Imprime los valores en USD de BTC y ETH
print('BTC: ', data['data']['BTC']['quote']['USD']['price'])
print('ETH: ', data['data']['ETH']['quote']['USD']['price'])