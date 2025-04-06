from flask import Flask
import redis

app = Flask(__name__)
redis_db = redis.Redis(host='redis') 

@app.route('/ping')
def ping():
  return {"status" : "ok"}

@app.route('/count')
def count():
  visits = redis_db.incr('visits')
  return {"count": visits}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
