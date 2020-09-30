import json

data='''
{
    {
        "id":"001",
        "X":"2",
        "name":"chuck"
    },
    {
        "id":"002",
        "X":"3"
        "name":"luck" 
    }
}
'''

info=json.loads(data)
print('name',info["name"])