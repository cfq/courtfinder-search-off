import requests

elasticurl = 'http://localhost:9200/courts'

r = requests.delete( elasticurl )
print r.status_code
print r.text