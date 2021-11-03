import time
from datetime import datetime
import requests
import json

delay = 1800 #seconds
discordWebhook = "https://discord.com/api/webhooks/905230201091416134/ePdWQ3EiFlYrxhAYQhG3l5UyJ_BiNH5zTl9i4nz7f5OFze4tdNHLFsCDwVIZBSNsvFnp" #enter in your webhook url
discordWebhook2 = "https://discord.com/api/webhooks/905229625259589693/1NwJmXbbhTC4uaHISWMgL3pswrmSOFx85SMhmQK4PKiyPkrOUtT28jbClEjbI9Nl59ws"

def getPrice(currency):
    priceUrl = 'https://api.coinbase.com/v2/prices/{}-USD/spot'.format(currency)
    r = requests.get(priceUrl)
    r = json.loads(r.text)
    return r['data']['amount']

while True:
    btc = getPrice('BTC')
    eth = getPrice('ETH')
    shib = getPrice('SHIB')
    sol = getPrice('SOL')
    jas = getPrice('JASMY')
    timestamp = datetime.utcnow().replace(microsecond=0).isoformat()
    embeds = [{
        'type': 'rich',
        "color": 123456,
        "timestamp": timestamp,
        "fields": [
          {
            "name": "BTC:",
            "value": '$' + str(btc),
            "inline": True
          },
          {
            "name": "ETH:",
            "value": '$' + str(eth),
            "inline": True

          },
          {
            "name": "SHIB:",
            "value": '$' + str(shib),
            "inline": True
          },
            {
              "name": "SOL:",
              "value": '$' + str(sol),
              "inline": True
            },
            {
              "name": "JASMY",
              "value": '$' + str(jas),
              "inline": True
            }
          ]
        }]
    payload = {"embeds": embeds}
    r = requests.post(discordWebhook,json=payload)
    r = requests.post(discordWebhook2,json=payload)
    print(timestamp) #print to console to make sure program isnt frozen
    time.sleep(delay)
