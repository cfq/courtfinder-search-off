from elasticsearch import Elasticsearch

def search( keyword ):
  es = Elasticsearch()

if __name__ == '__main__':
  keyword = raw_input("Search for: ")
  search( keyword )