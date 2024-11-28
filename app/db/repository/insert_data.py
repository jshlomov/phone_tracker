from datetime import datetime

from app.db.database import driver
from app.db.models.device import Device
from app.db.models.location import Location
from app.db.models.interaction import Interaction
from app.db.repository.device_repository import insert_device
from app.db.repository.interaction_repository import insert_interaction
from app.db.repository.location_repository import insert_location


def insert_device_location_interaction(from_device: Device, to_device: Device, from_location: Location,
                                       to_location: Location, interaction: Interaction):
    with driver.session() as session:
        from_device_id = from_device.id
        to_device_id = to_device.id
        query, params = insert_device(from_device)
        session.run(query, params)

        query, params = insert_location(from_device_id, from_location)
        session.run(query, params)

        query, params = insert_device(to_device)
        session.run(query, params)

        query, params = insert_location(to_device_id, to_location)
        session.run(query, params)

        query, params = insert_interaction(interaction)
        session.run(query, params)



