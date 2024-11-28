from datetime import datetime

from app.db.models.device import Device
from app.db.models.interaction import Interaction
from app.db.models.location import Location
from app.db.repository.insert_data import insert_device_location_interaction


def insert_data(json):
    from_device = Device(**{key: value for key, value in json['devices'][0].items() if key != "location"})
    to_device = Device(**{key: value for key, value in json['devices'][1].items() if key != "location"})
    from_location = Location(**json['devices'][0]['location'])
    to_location = Location(**json['devices'][1]['location'])
    interaction_data = json['interaction']
    interaction_data['timestamp'] = datetime.fromisoformat(interaction_data['timestamp'])
    interaction = Interaction(**interaction_data)

    insert_device_location_interaction(
        from_device,
        to_device,
        from_location,
        to_location,
        interaction
    )