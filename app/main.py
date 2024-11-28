from flask import Flask

from app.routes.device_route import device_blueprint

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(device_blueprint, url_prefix="/api/device")
    app.run()