from elasticsearch import Elasticsearch
from elasticsearch import helpers
import datetime
es = Elasticsearch()
#es.index(index="my-index",doc_type="test-type",body={"any":"data02",'a0':'b0',"timestamp":datetime.datetime.now()})
#es.index(index="my-index0",body={"any":"data02",'a0':'b0',"timestamp":datetime.datetime.now()})
res = es.search(index="my-index0")
#print(res)
print('*************')
def es_search(index,condition,value,lookup):
    body={             # 请求体
      "query": {       # 关键字，把查询语句给 query
          "bool": {    # 关键字，表示使用 filter 查询，没有匹配度
                "must": [      # 表示里面的条件必须匹配，多个匹配元素可以放在列表里
                    {
                        "match": {  # 关键字，表示需要匹配的元素
                            condition: value   # TransId 是字段名， 06100021650016153 是此字段需要匹配到的值
                        }
                    },
    ##                                    {
    ##                    "match": {  # 关键字，表示需要匹配的元素
    ##                        "a0": 'b0'   # TransId 是字段名， 06100021650016153 是此字段需要匹配到的值
    ##                    }
    ##                },
                     ],
                 "must_not": {   # 关键字，表示查询的结果里必须不匹配里面的元素
                        "match": {  # 关键字
                            "message": "M("    # message 字段名，这个字段的值一般是查询到的结果内容体。这里的意思是，返回的结果里不能包含特殊字符 'M('
                        }
                 }
            }
        },
        

      }
    response = es.search(
        index=index, # 索引名
        body=body

    )
    print(response,type(response))
    print('******************')
    print(response['hits']['hits'])
    result=[]
    for item in response['hits']['hits']:
        print(item['_source']['timestamp'])
        result.append(item['_source'][lookup])
    return result

print(es_search('my-index','any1','data02','timestamp'))
