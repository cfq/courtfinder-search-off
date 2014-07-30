import requests

elasticurl = 'http://localhost:9200/courtfinder'

r = requests.delete( elasticurl )
print r.status_code
print r.text
