from io import BytesIO

import redis
import requests
from flask import send_file, Flask


def create_app():
    app = Flask(__name__)
    redis_server = redis.StrictRedis(host='localhost', port=6379, db=2)

    @app.route('/img/<path:image_url>')
    def image(image_url):
        cached = redis_server.get(image_url)
        if cached:
            buffer_image = BytesIO(cached)
            buffer_image.seek(0)
        else:
            r = requests.get(image_url, headers={})
            buffer_image = BytesIO(r.content)
            buffer_image.seek(0)
            redis_server.setex(image_url, (60 * 60 * 24 * 7), buffer_image.getvalue())

        return send_file(buffer_image, mimetype='image/jpeg')

    return app
