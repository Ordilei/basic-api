from flask import Flask
from flask import request
import flask
import redis
import time
import json
from flask import Response, stream_with_context

app = Flask(__name__)
db = redis.Redis('redis') 

ttl = 31104000 

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@app.route('/api/', defaults={'path': ''}, methods = ['POST', 'GET'])
@app.route('/api/<path:path>', methods = ['POST', 'GET'])
def home(path):

    if (request.method == 'POST'):
        event = request.json
        event['last_updated'] = int(time.time())
        event['ttl'] = ttl
        db.delete(path)
        db.hmset(path, event)
        db.expire(path, ttl)
        return json.dumps(event), 201

    if not db.exists(path):
        return "Error: thing doesn't exist"

    event = db.hgetall(path)
    event["ttl"] = db.ttl(path)
    
    dict_with_ints = dict((k,int(v) if isInt(v) else v) for k,v in event.iteritems())
    return json.dumps(dict_with_ints), 200

@app.route('/projects', methods = ['GET'])
def projects():
    event = db.keys()
    body_all = []
    for unico in event:
      item = db.hgetall(unico)
      body_all.append(item)
      print body_all
    
    
    return json.dumps(body_all), 200

if __name__ == '__main__':
    app.run(port=8080, debug=false)
