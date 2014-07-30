import json, requests, sys

courts = None
proptypes = set()

elasticurl = 'http://localhost:9200/courtfinder/court/%s'

with open('./courts.json') as f:
  c = json.loads(f.read())
  f.close()
  courts = c['courts']

for c in courts:
  payload = json.dumps(c)
  cid = c['@id'].replace('/courts/', '')
  r = requests.put( elasticurl % cid, data=payload )

  print elasticurl % cid
  print r.status_code
  print r.text

  # cont = raw_input('Continue?')
  # if cont == 'n':
  #   sys.exit()
