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
