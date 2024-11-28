from flask import request, jsonify, Blueprint, Flask

from app.services.data_insertion_service import insert_data

phone_blueprint = Blueprint("phone", __name__)


@phone_blueprint.route("/api/phone_tracker", methods=['POST'])
def get_interaction():
   json = request.json
   print(json)
   insert_data(json)
   return jsonify({ }), 200

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(phone_blueprint)
    app.run()