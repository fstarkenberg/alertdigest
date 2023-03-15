from flask import Flask, request, jsonify
from redis import Redis
import logging
import os

app = Flask(__name__)

redis = Redis(host=os.environ.get("REDIS_HOST"), port=os.environ.get("REDIS_PORT", 6379))

@app.route('/')
def hello():
    redis.incr('hits')
    counter = str(redis.get('hits'),'utf-8')
    app.logger.debug('this is a DEBUG message')
    return "This webpage has been viewed "+counter+" time(s)"


@app.route('/healthz')
def flask_healthz():
	return "success"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9567, debug=True)
else:
    # Gunicorn
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

