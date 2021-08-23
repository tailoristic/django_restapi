import requests
import json

URL = "http://127.0.0.1:8000/stulist/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)

# GET API
get_data(2)


def post_data():
    data = {
        'name': 'Ravi',
        'roll': 211,
        'city': 'Umg'
    }
    
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)
    
# POST
# post_data()

def update_data():
    data = {
        'id': 10,
        'name': 'Kevin',
        'city': 'Delhi'
    }
    
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

# update PUT
# update_data()

def delete_data(id):
    data = {
        'id': id
    }
    
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)
    
# delete_data(10)