from elasticsearch import Elasticsearch
import pprint

es = Elasticsearch()
pp = pprint.PrettyPrinter(indent=4)

def search_keyword( keyword ):
    try:
        r = es.search("courtfinder", body={
            "query": {
                "multi_match": {
                    "query": keyword,
                    "fields": [ "name", "town", "streetAddress" ] 
                }
            }
        })

        return r["hits"]
    except:
        return False

if __name__ == '__main__':
  # keyword = raw_input("Search for: ")
  keyword = "gee"
  search( keyword )
