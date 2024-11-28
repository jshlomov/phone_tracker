from functools import partial

from toolz import pipe

from app.db.database import driver
from app.db.models.device import Device


def insert_device(device: Device):
    query = """
        MERGE (d:Device {
            id: $id,
            name: $name,
            brand: $brand,
            model: $model,
            os: $os
            }
        )
        RETURN d
    """
    params = {
        "id": device.id,
        "name": device.name,
        "brand": device.brand,
        "model": device.model,
        "os": device.os
    }
    return query, params

def find_bluetooth_connected_devices():
    with driver.session() as session:
        query = """
            MATCH (start:Device)
            MATCH (end:Device)
            WHERE start <> end
            MATCH path = shortestPath((start)-[:CONNECTED*]->(end))
            WHERE ALL(r IN relationships(path) WHERE r.method = 'Bluetooth')
            WITH path, length(path) as len
            ORDER BY len DESC
            RETURN path, len
        """
        return session.run(query).data()


def find_strong_signal_connections():
    with driver.session() as session:
        query = """
            MATCH (start:Device)
            MATCH (end:Device)
            WHERE start <> end
            MATCH path = shortestPath((start)-[:CONNECTED*]->(end))
            WHERE ALL(r IN relationships(path) WHERE r.signal_strength_dbm > -60)
            WITH path, length(path) as len
            ORDER BY len DESC
            RETURN path, len
        """
        return session.run(query).data()

def count_connected_devices(device_id):
    with driver.session() as session:
        query = """
            MATCH (d:Device {id: $device_id})<-[:CONNECTED]-(connected:Device)
            RETURN count(DISTINCT connected) AS connected_count
        """
        result = session.run(query, {"device_id": device_id}).single()

        if result:
            return result["connected_count"]
        else:
            raise Exception(f"No device found with ID {device_id}")

def check_direct_connection(device_1_id, device_2_id):
    with driver.session() as session:
        query = """
            MATCH (d1:Device {id: $device_1_id})-[:CONNECTED]->(d2:Device {id: $device_2_id})
            RETURN COUNT(d1) AS connection_exists
        """
        params = {
            "device_1_id": device_1_id,
            "device_2_id": device_2_id
        }
        result = session.run(query, params).single()

        return result["connection_exists"] > 0

def get_most_recent_interaction(device_id):
    try:
        with driver.session() as session:
            query = """
                MATCH (d:Device {id: $device_id})-[rel:CONNECTED]->(d2:Device)
                RETURN d, rel, d2
                ORDER BY rel.timestamp DESC
                LIMIT 1
            """
            params = {"device_id": device_id}
            result = session.run(query, params).data()
            return result
    except Exception as e:
        raise RuntimeError(f"An error occurred {str(e)}")

print(get_most_recent_interaction("2da5382c-8a3c-436f-8710-3a9df07afde2"))