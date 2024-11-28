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
            MATCH path = (d1:Device)-[:CONNECTED*]->(d2:Device)
            WHERE ALL(r IN relationships(path) WHERE r.method = 'Bluetooth')
            RETURN path, length(path) as len
        """
        results = session.run(query)

        connections = []
        for record in results:
            path_nodes = [Device(**node) for node in record["path"].nodes]
            path_length = record["len"]
            connections.append({
                "devices": path_nodes,
                "path_length": path_length
            })
        return connections


def find_strong_signal_connections():
    with driver.session() as session:
        query = """
            MATCH (d1:Device)-[c:CONNECTED]->(d2:Device)
            WHERE c.signal_strength_dbm > -60
            RETURN d1, d2
        """
        results = session.run(query).data()

        return pipe(
            results,
            partial(map, lambda x: {"devices" : [Device(**x["d1"]), Device(**x["d2"])]}),
            list
        )

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