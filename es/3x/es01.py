from elasticsearch import Elasticsearch

# es = Elasticsearch(hosts="",http_auth=('',''))
es = Elasticsearch(hosts='http://localhost:9200',http_auth=('elasticsearch','Eolc9q6fTsu0QXiCGMlvUw'))
print(es.info())

