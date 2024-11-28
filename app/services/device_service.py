import app.db.repository.device_repository as device_rep


def find_bluetooth_connected_devices():
    return device_rep.find_bluetooth_connected_devices()

def find_strong_signal_connections():
    return device_rep.find_strong_signal_connections()

def count_connected_devices(device_id):
    try:
        return device_rep.count_connected_devices(device_id)
    except Exception as e:
        return str(e)

def check_direct_connection(json):
    device_1_id = json['device_1_id']
    device_2_id = json['device_2_id']
    return device_rep.check_direct_connection(device_1_id, device_2_id)

def get_most_recent_interaction(device_id):
    try:
        return device_rep.get_most_recent_interaction(device_id)
    except Exception as e:
        return str(e)
