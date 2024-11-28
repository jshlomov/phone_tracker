from flask import jsonify, Blueprint, request
import app.services.device_service as device_service

device_blueprint = Blueprint("device", __name__)

@device_blueprint.route('/connected-devices/bluetooth', methods=['GET'])
def find_bluetooth_connected_devices():
    return jsonify(device_service.find_bluetooth_connected_devices()), 200


@device_blueprint.route('/connected-devices/signal-strength', methods=['GET'])
def find_strong_signal_connections():
    return jsonify(device_service.find_strong_signal_connections()), 200


@device_blueprint.route('/connected-count/<device_id>', methods=['GET'])
def count_connected_devices(device_id):
    return jsonify(device_service.count_connected_devices(device_id)), 200


@device_blueprint.route('/connected', methods=['POST'])
def check_direct_connection():
    json = request.json
    return jsonify(device_service.check_direct_connection(json)), 200





