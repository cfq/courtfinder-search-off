import json, requests, sys

courts = None
proptypes = set()

elasticurl = 'http://localhost:9200/courts/court/%s'

with open('./courts.json') as f:
  c = json.loads(f.read())
  f.close()
  courts = c['courts']

cid = 0
for c in courts:
  payload = json.dumps(c)
  r = requests.put( elasticurl % cid, data=payload )
  cid += 1

  print elasticurl % cid
  print r.status_code
  print r.text

  # cont = raw_input('Continue?')
  # if cont == 'n':
  #   sys.exit()