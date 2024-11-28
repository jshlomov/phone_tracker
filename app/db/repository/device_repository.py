from app.db.database import driver
from app.db.models.device import Device


def insert_device(device: Device):
    with driver.session() as session:
        query = """
            MERGE (d:Device {
                id: $id,
                brand: $brand,
                model: $model,
                os: $os
                }
            )
            RETURN d
        """
        params = {
            "id": device.id,
            "brand": device.brand,
            "model": device.model,
            "os": device.os
        }
        res = session.run(query, params)
        return res


