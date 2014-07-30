import json, requests, sys
import psycopg2

courts = None
proptypes = set()

elasticurl = 'http://localhost:9200/courtfinder/court/%s'
conn = psycopg2.connect("dbname='courtfinder_development' user='mehmet' host='localhost' password=''")


def load_all():
  with open('./courts.json') as f:
    c = json.loads(f.read())
    f.close()
    courts = c['courts']

  for c in courts:
    slug = c['@id'].replace('/courts/', '')
    c['postcodes'] = get_postcodes( slug )
    c['areas_of_law'] = get_areas_of_law( slug )
    payload = json.dumps(c)
    cid = c['@id'].replace('/courts/', '')
    r = requests.put( elasticurl % cid, data=payload )

    print elasticurl % cid
    print r.status_code
    print r.text


def get_postcodes( slug ):
  sql = """SELECT c.id, p.postcode 
             FROM courts as c, postcode_courts as p 
            WHERE p.court_id = c.id AND c.slug = '%s'"""

  cur = conn.cursor()
  cur.execute( sql % slug )
  return [postcode for cid, postcode in cur.fetchall()]


def get_areas_of_law( slug ):
  sql = """SELECT c.name, a.name
             FROM courts as c, areas_of_law as a, courts_areas_of_law as ac
            WHERE ac.court_id = c.id
              AND ac.area_of_law_id = a.id
              AND c.slug = '%s'"""

  cur = conn.cursor()
  cur.execute( sql % slug )
  return [aol for cid, aol in cur.fetchall()]



if __name__ == '__main__':
  load_all()