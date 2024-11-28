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


